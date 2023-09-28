import random
import time

import numpy as np
from sklearn.metrics import mean_squared_error
from algoritmos import Compilado, compilados_ordenados_de_forma_optima
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import seaborn as sns
from scipy.stats import gaussian_kde

def tiempo_ejecucion(compilados):
    tiempo_inicial = time.process_time()
    compilados_ordenados_de_forma_optima(compilados)
    tiempo_final = time.process_time()
    return tiempo_final - tiempo_inicial


def generar_compilados_aleatorios(cant_compilados):
    compilados = []
    for _ in range(cant_compilados):
        compilados.append(Compilado(random.randint(1, 99999), random.randint(1, 99999)))
    return compilados


def main():
    graficar_simulaciones(400, 1, "./informe/img/tiempos_valores_bajos.png", 20, 10, 40)
    #graficar_simulaciones(10000, 50, "./informe/img/tiempos_valores_altos.png", 10, 12, 20)


def graficar_simulaciones(maximo, intervalos, path_salida, numero_vueltas, numero_muestras_por_cantidad, group_size):
    cantidad_compilados = list(range(1, maximo, intervalos))
    muestras_compialados = []

    mediciones = []
    for i in range(numero_muestras_por_cantidad):
        muestra_muestras_compialados = []
        mediciones_aux = []
        for cantidad in cantidad_compilados:
            muestra_muestras_compialados.append(generar_compilados_aleatorios(cantidad))
            mediciones_aux.append(0)
        muestras_compialados.append(muestra_muestras_compialados)
        mediciones.append(mediciones_aux)

    for vuelta in range(numero_vueltas):
        for index_muestras, muestras in enumerate(muestras_compialados):
            for index_muestra, muestra in enumerate(muestras):
                mediciones[index_muestras][index_muestra] += tiempo_ejecucion(muestra) * 1000
    
    
    for vuelta in range(numero_vueltas):
        for index_muestras, muestras in enumerate(muestras_compialados):
            for index_muestra, muestra in enumerate(muestras):
                mediciones[index_muestras][index_muestra] /= numero_vueltas
    
    tiempos_ejecucion = [item for sublist in mediciones for item in sublist]
    cantidad_compilados = cantidad_compilados * numero_vueltas

    
    x = cantidad_compilados  # Example unsorted x values
    y = tiempos_ejecucion  # Corresponding y values

    # Pair x and y values and sort based on x
    sorted_pairs = sorted(zip(x, y), key=lambda pair: pair[0])

    # Unzip the sorted pairs back into separate x and y arrays
    sorted_x, sorted_y = zip(*sorted_pairs)

    x = np.array(sorted_x)
    y = np.array(sorted_y)

    # Regresión Lineal
    coefficients = np.polyfit(x, y, 1)
    slope, intercept = coefficients
    linear_regression_line = slope * x + intercept

    # Calcular el RMSE (Root mean square error) para la regresión lineal
    rmse_recta_lineal = np.sqrt(mean_squared_error(y, linear_regression_line)) * pow(10, 30)
    print(f"RMSE para la recta lineal: {rmse_recta_lineal}")

    # Regresión lineal Logarítmica
    def n_logn_function(x, a, b):
        return a * x * np.log(x) + b

    params, _ = curve_fit(n_logn_function, x, y)
    a = params[0]
    b = params[1]
    logaritmic_regression_line = a * x * np.log(x) + b

    # Calcular el RMSE (Root mean square error) para la regresión lineal logarítmica
    rmse_funcion_lineal_log = np.sqrt(mean_squared_error(y, logaritmic_regression_line)) * pow(10, 30)
    print(f"RMSE para la función lineal logarítmica: {rmse_funcion_lineal_log}")

    X = np.array(x)
    Y = np.array(y)

    # Determine the number of overlapping groups
    num_groups = len(x) - group_size + 1

    # Initialize arrays to store quantiles
    quantiles_10 = np.zeros(num_groups)
    quantiles_90 = np.zeros(num_groups)

    # Calculate quantiles for each group
    for i in range(num_groups):
        group_y = Y[i:i+group_size]
        quantiles_10[i] = np.percentile(group_y, 10)
        quantiles_90[i] = np.percentile(group_y, 90)
       
    # Determine the center positions for each group
    group_centers = []
    for i in range(num_groups):
        group_center = np.mean(X[i:i+group_size])
        group_centers.append(group_center)

    group_centers = np.array(group_centers)

    # Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents
    nbins=1200
    k = gaussian_kde([x,y])
    xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))

    # Graficar
    plt.figure(dpi=1000)
    
    # Make the plot
    plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='auto')

    # # Plot the lines
    # plt.plot(group_centers, quantiles_10, label='Q0.10', color="greenyellow", linewidth=0.75)
    # plt.plot(group_centers, quantiles_90, label='Q0.90', color="violet", linewidth=0.75)

    # # plt.scatter(
    # #     x, y, label="Tiempo de ejecución", marker="o", color="darkcyan", alpha=0.5, s=0.5
    # # )
    # plt.plot(
    #     x,
    #     linear_regression_line,
    #     label="Regresión Linear",
    #     linestyle="-",
    #     color="lightcoral",
    #     linewidth=1,
    # )
    # plt.plot(
    #     x,
    #     logaritmic_regression_line,
    #     label="Regresión n log n",
    #     linestyle="-",
    #     color="navy",
    #     linewidth=1,
    # )

    # Anotamos el rmse de cada regresión
    plt.annotate(
        f"RMSE recta lineal: {rmse_recta_lineal:.5f}",
        (0.02, 0.75),
        xycoords="axes fraction",
        fontsize=8,
        color="lightcoral",
    )

    plt.annotate(
        f"RMSE n log n: {rmse_funcion_lineal_log:.5f}",
        (0.02, 0.70),
        xycoords="axes fraction",
        fontsize=8,
        color="navy",
    )

    # Etiquetas y leyenda
    plt.xlabel("Cantidad de compilados")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.legend()
    plt.title("Tiempo de ejecución del algoritmo de ordenamiento")
    plt.savefig(path_salida)


main()
