import time

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit

from backtracking import bracktracking_hitting_set_problem
from generador_de_ejemplos import generar_ejemplos


def tiempo_ejecucion_y_resultado(solicitudes, algoritmo):
    tiempo_inicial = time.process_time()
    resultado = algoritmo(solicitudes)
    tiempo_final = time.process_time()
    return tiempo_final - tiempo_inicial, resultado


def graficar_simulaciones(maximo, cant_por_prensa, algoritmo, path_salida):
    mediciones = []

    # Generamos las mediciones de tiempo por cada generación de ejemplo
    for i in range(1, maximo, 10):
        solicitudes = generar_ejemplos(i, cant_por_prensa, True)

        # Calculamos el tiempo de ejecución del algoritmo para el ejemplo generado
        tiempo, _ = tiempo_ejecucion_y_resultado(solicitudes, algoritmo)
        mediciones.append((i, tiempo))

    # Separamos los valores de x e y
    x = [medicion[0] for medicion in mediciones]
    y = [medicion[1] for medicion in mediciones]

    # Exportamos los gráficos
    exportar_grafico_puntos(x, y, path_salida)


def exportar_grafico_puntos(x, y, path_salida):
    plt.figure()
    x_numpy = np.array(x)
    y_numpy = np.array(y)

    # Ajuste de la curva exponencial
    parametros_optimos_exp, _ = curve_fit(
        funcion_exponencial, x_numpy, y_numpy)

    # Ajuste de la curva lineal
    parametros_optimos_lin, _ = curve_fit(funcion_lineal, x_numpy, y_numpy)

    x_curva = np.linspace(min(x), max(x), 100)

    # Graficar la curva exponencial ajustada
    y_curva_exp = funcion_exponencial(x_curva, *parametros_optimos_exp)
    plt.plot(x_curva, y_curva_exp, label='Curva Exponencial', color='red')

    # Graficar la curva lineal ajustada
    y_curva_lin = funcion_lineal(x_curva, *parametros_optimos_lin)
    plt.plot(x_curva, y_curva_lin, label='Curva Lineal', color='green')

    # Graficar los puntos
    plt.scatter(x, y, label='Mediciones', color='blue')

    # Calculamos el error cuadrático medio
    error_exp = mean_squared_error(y, y_curva_exp)
    error_lin = mean_squared_error(y, y_curva_lin)

    # Ponemos en el gráfico el error cuadrático medio
    plt.text(0.1, 0.9, f"Error cuadrático medio exponencial: {error_exp}",
             horizontalalignment='center',
             verticalalignment='center',
             transform=plt.gca().transAxes)

    plt.text(0.1, 0.8, f"Error cuadrático medio lineal: {error_lin}",
             horizontalalignment='center',
             verticalalignment='center',
             transform=plt.gca().transAxes)

    # Etiquetas y leyenda
    plt.xlabel("Cantidad de prensas")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.legend()
    plt.title(
        "Mediciones de tiempo de ejecución del algoritmo de Backtracking")
    plt.savefig(path_salida)


def funcion_exponencial(x, a, b):
    return a * np.exp(b * x)


def funcion_lineal(x, a, b):
    return a * x + b


# graficar_simulaciones(
#     100, 10, bracktracking_hitting_set_problem, "medicion_tiempo.png")
