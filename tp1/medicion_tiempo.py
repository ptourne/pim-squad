import random
import time

import numpy as np
from sklearn.metrics import mean_squared_error
from algoritmos import Compilado, compilados_ordenados_de_forma_optima
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

CANTIDAD_PARA_PROMEDIO = 3
CANTIDAD_COMPILADOS = 1500


def tiempo_ejecucion(compilados):
    tiempo_inicial = time.time()
    compilados_ordenados_de_forma_optima(compilados)
    tiempo_final = time.time()
    return tiempo_final - tiempo_inicial


def generar_compilados_aleatorios(cant_compilados):
    compilados = []
    for _ in range(cant_compilados):
        compilados.append(Compilado(random.randint(1, 99999), random.randint(1, 99999)))
    return compilados


def main():
    graficar_simulaciones(1501, 1, "./informe/img/tiempos_valores_bajos.png")
    graficar_simulaciones(10000, 2, "./informe/img/tiempos_valores_altos.png")


def graficar_simulaciones(maximo, intervalos, path_salida):
    cantidad_compilados = range(1, maximo, intervalos)
    tiempos_ejecucion = []

    for i in cantidad_compilados:
        compilados_ejemplo = generar_compilados_aleatorios(i)
        tiempos_ejecucion.append(tiempo_ejecucion(compilados_ejemplo) * 1000)

    x = np.array(cantidad_compilados)
    y = np.array(tiempos_ejecucion)

    # Regresión Lineal
    coefficients = np.polyfit(x, y, 1)
    slope, intercept = coefficients
    linear_regression_line = slope * x + intercept

    # Calcular el RMSE (Root mean square error) para la regresión lineal
    rmse_recta_lineal = np.sqrt(mean_squared_error(y, linear_regression_line))
    print(f"RMSE para la recta lineal: {rmse_recta_lineal}")

    # Regresión lineal Logarítmica
    def n_logn_function(x, a, b):
        return a * x * np.log(x) + b

    params, _ = curve_fit(n_logn_function, x, y)
    a = params[0]
    b = params[1]
    logaritmic_regression_line = a * x * np.log(x) + b

    # Calcular el RMSE (Root mean square error) para la regresión lineal logarítmica
    rmse_funcion_lineal_log = np.sqrt(mean_squared_error(y, logaritmic_regression_line))
    print(f"RMSE para la función lineal logarítmica: {rmse_funcion_lineal_log}")

    X = np.array(x)
    Y = np.array(y)

    # Define the size of the overlapping groups
    group_size = 15

    # Determine the number of overlapping groups
    num_groups = len(x) - group_size + 1

    # Initialize arrays to store quantiles
    quantiles_25 = np.zeros(num_groups)
    quantiles_50 = np.zeros(num_groups)
    quantiles_75 = np.zeros(num_groups)

    # Calculate quantiles for each group
    for i in range(num_groups):
        group_y = Y[i:i+group_size]
        quantiles_25[i] = np.percentile(group_y, 25)
        quantiles_50[i] = np.percentile(group_y, 50)
        quantiles_75[i] = np.percentile(group_y, 75)


        

    # Graficar
    plt.figure(dpi=600)
    # Plot the lines
    plt.plot(X[group_size-1:], quantiles_25, label='Q0.25')
    plt.plot(X[group_size-1:], quantiles_50, label='Q0.50')
    plt.plot(X[group_size-1:], quantiles_75, label='Q0.75')

    plt.scatter(
        x, y, label="Tiempo de ejecución", marker="o", color="darkcyan", alpha=0.35, s=4
    )
    plt.plot(
        x,
        linear_regression_line,
        label="Regresión Linear",
        linestyle="-",
        color="lightcoral",
        linewidth=2.0,
    )
    plt.plot(
        x,
        logaritmic_regression_line,
        label="Regresión n log n",
        linestyle="-",
        color="navy",
        linewidth=2.0,
    )

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
