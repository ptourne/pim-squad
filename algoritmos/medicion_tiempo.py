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
    graficar_simulaciones(1000, 1, "./informe/img/tiempos_valores_bajos_puntos.png", "./informe/img/tiempos_valores_bajos_densidad.png", 20, 20, 100)
    graficar_simulaciones(10000, 10, "./informe/img/tiempos_valores_altos_puntos.png", "./informe/img/tiempos_valores_altos_densidad.png", 20, 8, 150)


def graficar_simulaciones(maximo, intervalos, path_salida_puntos, path_salida_densidad, numero_vueltas, numero_muestras_por_cantidad, group_size):
    cantidad_compilados = list(range(1, maximo, intervalos))
    muestras_compilados = []
    mediciones = []

    # Se genera la matriz <muestras_compilados> de tamaño [numero_muestras_por_cantidad][len(cantidad_compilados)]
    # la cual contiene por cada cantidad de comilados, numero_muestras_por_cantidad diferentes escenarios. 
    # Además, se inicializa una matriz de mediciones de igual tamaño con ceros.
    for i in range(numero_muestras_por_cantidad):
        escenarios_muestras_compilados = []
        mediciones_aux = []
        for cantidad in cantidad_compilados:
            escenarios_muestras_compilados.append(generar_compilados_aleatorios(cantidad))
            mediciones_aux.append(0)
        muestras_compilados.append(escenarios_muestras_compilados)
        mediciones.append(mediciones_aux)

    # Se recorre la matriz de muestras y se mide el tiempo de ordenamiento para cada una, vuelta veces
    # sumando cada medición al casillero correspondiente en la matriz mediciones.
    for vuelta in range(numero_vueltas):
        for index_muestras_por_cantidad, muestras_por_cantidad in enumerate(muestras_compilados):
            for index_muestra, muestra in enumerate(muestras_por_cantidad):
                mediciones[index_muestras_por_cantidad][index_muestra] += tiempo_ejecucion(muestra) * 1000
    
    # Se recorre la matriz de mediciones dividiendo cada casillero por numero_vueltas para obtener
    # el promedio de las mediciones
    for index_muestras_por_cantidad, muestras_por_cantidad in enumerate(muestras_compilados):
        for index_muestra, muestra in enumerate(muestras_por_cantidad):
            mediciones[index_muestras_por_cantidad][index_muestra] /= numero_vueltas
    

    # Se aplana la matriz mediciones y se concatena cantidad_compilados numero_vueltas veces
    tiempos_ejecucion = [item for sublist in mediciones for item in sublist]
    cantidad_compilados = cantidad_compilados * numero_vueltas

    # Agrupamos al vector de mediciones y al vector de cantidad de compilados para esa medición
    # para poder odernarlos de tal manera que la cantidad quede en forma creciente.
    # Luego los desagrupamos
    sorted_pairs = sorted(zip(cantidad_compilados, tiempos_ejecucion), key=lambda pair: pair[0])
    cantidad_compilados_ordenados, tiempos_ejecucion_ordenados = zip(*sorted_pairs)

    x = np.array(cantidad_compilados_ordenados)
    y = np.array(tiempos_ejecucion_ordenados)


    exportar_grafico_puntos(x, y, group_size, path_salida_puntos)
    exportar_grafico_densidad(x, y, path_salida_densidad)

def exportar_grafico_puntos(x, y, tamanio_grupos_cuantiles, path_salida):
    # Graficar
    plt.figure(dpi=800)

    X = np.array(x)
    Y = np.array(y)

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

    # Determinar número de grupos
    num_groupos = len(x) - tamanio_grupos_cuantiles + 1

    # Inicializar arreglos para almacenar cuantiles
    cuantiles_10 = np.zeros(num_groupos)
    cuantiles_90 = np.zeros(num_groupos)

    centros_grupos = []

    # Calcular cuantiles para cada grupo y el centro de cada uno
    for i in range(num_groupos):
        group_y = Y[i:i+tamanio_grupos_cuantiles]
        cuantiles_10[i] = np.percentile(group_y, 10)
        cuantiles_90[i] = np.percentile(group_y, 90)
        centro_grupo = np.mean(X[i:i+tamanio_grupos_cuantiles])
        centros_grupos.append(centro_grupo)

    centros_grupos = np.array(centros_grupos)
    # Plot the lines
    plt.plot(centros_grupos, cuantiles_90, label='Q0.90', color="darkgreen", linewidth=0.75)
    plt.plot(centros_grupos, cuantiles_10, label='Q0.10', color="firebrick", linewidth=0.75)

    plt.scatter(
        x, y, label="Tiempo de ejecución", marker="o", color="lightsteelblue", alpha=0.7, s=0.8
    )
    plt.plot(
        x,
        linear_regression_line,
        label="Regresión Linear",
        linestyle="-",
        color="darkmagenta",
        linewidth=1,
    )
    plt.plot(
        x,
        logaritmic_regression_line,
        label="Regresión n log n",
        linestyle="-",
        color="navy",
        linewidth=1,
    )

    # Anotamos el rmse de cada regresión
    plt.annotate(
        f"RMSE recta lineal: {rmse_recta_lineal:.5f}",
        (0.02, 0.62),
        xycoords="axes fraction",
        fontsize=8,
        color="darkmagenta",
    )

    plt.annotate(
        f"RMSE n log n: {rmse_funcion_lineal_log:.5f}",
        (0.02, 0.57),
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


def exportar_grafico_densidad(x, y, path_salida):
    # Graficar
    plt.figure(dpi=800)

    X = np.array(x)
    Y = np.array(y)

    # Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents
    nbins=1200
    k = gaussian_kde([x,y])
    xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))
    
    # Make the plot
    c = plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='auto', cmap='Blues')
    plt.colorbar(c, format='')

    # Etiquetas y leyenda
    plt.xlabel("Cantidad de compilados")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.legend()
    plt.title("Densidad de mediciones de tiempo de ejecución del algoritmo de ordenamiento")
    plt.savefig(path_salida)


main()
