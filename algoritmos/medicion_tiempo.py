import time

import numpy as np
import matplotlib.pyplot as plt
from backtracking import bracktracking_hitting_set_problem
from greedy import aproximacion_greedy_maximo_global_con_recalculo
from programacion_lineal_continua import hitting_set_pl_continua
from programacion_lineal_entera import hitting_set_pl_entera

from generador_de_ejemplos import generar_ejemplos


def tiempo_ejecucion_y_resultado(solicitudes, algoritmo):
    tiempo_inicial = time.process_time()
    resultado = algoritmo(solicitudes)
    tiempo_final = time.process_time()
    return tiempo_final - tiempo_inicial, resultado


def graficar_simulaciones(maximo, cant_por_prensa, path_salida):
    mediciones_back = []
    mediciones_lin_ent = []
    mediciones_lin_cont = []
    mediciones_greedy = []

    # Generamos las mediciones de tiempo por cada generación de ejemplo
    for i in range(1, maximo, 10):
        solicitudes = generar_ejemplos(i, cant_por_prensa, True)

        # tiempo, _ = tiempo_ejecucion_y_resultado(
        #     solicitudes, bracktracking_hitting_set_problem
        # )
        # mediciones_back.append((i, tiempo))

        tiempo, _ = tiempo_ejecucion_y_resultado(
            solicitudes, hitting_set_pl_entera)
        mediciones_lin_ent.append((i, tiempo))

        tiempo, _ = tiempo_ejecucion_y_resultado(
            solicitudes, hitting_set_pl_continua)
        mediciones_lin_cont.append((i, tiempo))

        tiempo, _ = tiempo_ejecucion_y_resultado(
            solicitudes, aproximacion_greedy_maximo_global_con_recalculo
        )
        mediciones_greedy.append((i, tiempo))

    # Separamos los valores de x e y
    x_back = [medicion[0] for medicion in mediciones_back]
    y_back = [medicion[1] for medicion in mediciones_back]

    x_lin_ent = [medicion[0] for medicion in mediciones_lin_ent]
    y_lin_ent = [medicion[1] for medicion in mediciones_lin_ent]

    x_lin_cont = [medicion[0] for medicion in mediciones_lin_cont]
    y_lin_cont = [medicion[1] for medicion in mediciones_lin_cont]

    x_greedy = [medicion[0] for medicion in mediciones_greedy]
    y_greedy = [medicion[1] for medicion in mediciones_greedy]

    # Exportamos los gráficos
    exportar_grafico_puntos(
        x_back,
        y_back,
        x_lin_ent,
        y_lin_ent,
        x_lin_cont,
        y_lin_cont,
        x_greedy,
        y_greedy,
        path_salida,
    )


def exportar_grafico_puntos(
    x_back,
    y_back,
    x_lin_ent,
    y_lin_ent,
    x_lin_cont,
    y_lin_cont,
    x_greedy,
    y_greedy,
    path_salida,
):
    plt.figure()
    x_numpy_back = np.array(x_back)
    y_numpy_back = np.array(y_back)

    x_numpy_lin_ent = np.array(x_lin_ent)
    y_numpy_lin_ent = np.array(y_lin_ent)

    x_numpy_lin_cont = np.array(x_lin_cont)
    y_numpy_lin_cont = np.array(y_lin_cont)

    x_numpy_greedy = np.array(x_greedy)
    y_numpy_greedy = np.array(y_greedy)

    # Ponemos los puntos no tan oscuros
    plt.plot(x_numpy_back, y_numpy_back, "o", alpha=0.5)
    plt.plot(x_numpy_lin_ent, y_numpy_lin_ent, "o", alpha=0.5)
    plt.plot(x_numpy_lin_cont, y_numpy_lin_cont, "o", alpha=0.5)
    plt.plot(x_numpy_greedy, y_numpy_greedy, "o", alpha=0.5)

    # Configurar el gráfico
    plt.xlabel("Cantidad de solicitudes")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución de los algoritmos")
    plt.legend()
    plt.show()


def main():
    graficar_simulaciones(10000, 100, "medicion_tiempo.png")


main()
