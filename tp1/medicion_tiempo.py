import time
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error
from algoritmos import Compilado, compilados_ordenados_de_forma_optima

PROMEDIO_CANT_COMPI_IGUALES = 5
PROMEDIO_CANT_COMPI_DISTINTOS = 5
CANTIDAD_COMPILADOS_MAX = 10000


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
    cantidad_compilados = range(1, CANTIDAD_COMPILADOS_MAX + 1)
    tiempos_ejecucion = []

    for i in range(1, CANTIDAD_COMPILADOS_MAX + 1):
        tiempos_ejecucion_aux = []

        for _ in range(1, PROMEDIO_CANT_COMPI_DISTINTOS):
            tiempos_ejecucion_vuelta = [None] * PROMEDIO_CANT_COMPI_IGUALES
            compilados_ejemplo = generar_compilados_aleatorios(i)

            for j in range(PROMEDIO_CANT_COMPI_IGUALES):
                tiempos_ejecucion_vuelta[j] = (
                    tiempo_ejecucion(compilados_ejemplo) * 1000
                )

            tiempos_ejecucion_aux.append(np.mean(tiempos_ejecucion_vuelta))
        tiempos_ejecucion.append(np.mean(tiempos_ejecucion_aux))

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

    # Graficar
    plt.figure(dpi=600)
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
    plt.savefig("tiempos_ejecucion.png")

    # Ahora guardamos el gráfico con un zoom en los primeros valores para notar una "panza" en la función n log n
    plt.xlim(-200, 2000)
    plt.ylim(-0.1, 0.4)
    plt.savefig("tiempos_ejecucion_zoom_bajos.png")

    # Ahora guardamos el gráfico con un zoom en los valores altos de cantidades de compilados para notar la tendencia lineal
    plt.xlim(8000, CANTIDAD_COMPILADOS_MAX)
    plt.ylim(0.7, 2)
    plt.savefig("tiempos_ejecucion_zoom_altos.png")


main()
