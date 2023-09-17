import random
import time

import numpy as np
from algoritmos import Compilado, compilados_ordenados_de_forma_optima
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


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
    cantidad_compilados = []
    tiempos_ejecucion = []

    for cantidad in range(1, 10000, 10):
        compilados_ejemplo = generar_compilados_aleatorios(cantidad)
        cantidad_compilados.append(cantidad)
        tiempos_ejecucion.append(tiempo_ejecucion(compilados_ejemplo) * 1000)

    x = np.array(cantidad_compilados)
    y = np.array(tiempos_ejecucion)

    # Regresión Lineal
    coefficients = np.polyfit(x, y, 1)
    slope, intercept = coefficients
    linear_regression_line = slope * x + intercept

    # Regresión lineal Logarítmica
    def n_logn_function(x, a):
        return a * x * np.log(x)

    params, _ = curve_fit(n_logn_function, x, y)
    a = params[0]
    logaritmic_regression_line = a * x * np.log(x)

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

    # Etiquetas y leyenda
    plt.xlabel("Cantidad de compilados")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.legend()
    plt.title("Tiempo de ejecución del algoritmo de ordenamiento")
    plt.savefig("tiempos_ejecucion.png")


main()
