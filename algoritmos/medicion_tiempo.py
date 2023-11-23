import argparse
import time

import numpy as np
import matplotlib.pyplot as plt
from backtracking import bracktracking_hitting_set_problem
from greedy import aproximacion_greedy_maximo_por_grupos
from programacion_lineal_continua import hitting_set_pl_continua
from programacion_lineal_entera import hitting_set_pl_entera

from generador_de_ejemplos import generar_ejemplos_abc


def tiempo_ejecucion_y_resultado(solicitudes, algoritmo):
    tiempo_inicial = time.process_time()
    resultado = algoritmo(solicitudes)
    tiempo_final = time.process_time()
    return tiempo_final - tiempo_inicial, resultado


def graficar_simulaciones(maximo=10, cant_por_conjunto=3, path_salida="medicion_prueba", step=1):
    mediciones_back = []
    mediciones_lin_ent = []
    mediciones_lin_cont = []
    mediciones_greedy = []

    # Generamos las mediciones de tiempo por cada generación de ejemplo
    for i in range(1, maximo, step):
        solicitudes = generar_ejemplos_abc(i, 3, 1, cant_por_conjunto, True, i)

        tiempo, _ = tiempo_ejecucion_y_resultado(
            solicitudes, bracktracking_hitting_set_problem
        )
        mediciones_back.append((i, tiempo))

        tiempo, solucion = tiempo_ejecucion_y_resultado(
            solicitudes, hitting_set_pl_entera)
        mediciones_lin_ent.append((i, tiempo))

        tiempo, _ = tiempo_ejecucion_y_resultado(
            solicitudes, hitting_set_pl_continua)
        mediciones_lin_cont.append((i, tiempo))

        tiempo, _ = tiempo_ejecucion_y_resultado(
            solicitudes, aproximacion_greedy_maximo_por_grupos
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

    # Puntos reales
    plt.scatter(x_back, y_back, label="Backtracking", color='red')
    plt.scatter(x_lin_ent, y_lin_ent,
                label="Programación Lineal Entera", color='green')
    plt.scatter(x_lin_cont, y_lin_cont,
                label="Programación Lineal Continua", color='blue')
    plt.scatter(x_greedy, y_greedy, label="Greedy", color='purple')

    # Ponemos la leyenda
    plt.plot(x_numpy_back, y_numpy_back, color='red')
    plt.plot(x_numpy_lin_ent, y_numpy_lin_ent, color='green')
    plt.plot(
        x_numpy_lin_cont, y_numpy_lin_cont, color='blue'
    )
    plt.plot(x_numpy_greedy, y_numpy_greedy, color='purple')

    # Configurar la escala logarítmica en el eje y
    # plt.yscale("log")

    # Configurar el gráfico
    plt.xlabel("Cantidad de solicitudes")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución de los algoritmos")
    plt.legend()

    # Guardar el gráfico
    plt.savefig(path_salida)


def main():
    parser = argparse.ArgumentParser(
        description="Guarda en un archivo un gráfico con los tiempos de ejecución de los algoritmos"
    )

    parser.add_argument(
        "direccion_salida",
        metavar="archivo",
        type=str,
        nargs=1,
        help="Dirección del archivo de salida con los resultados de la comparación",
    )

    parser.add_argument(
        "--maximo",
        metavar="maximo",
        type=int,
        nargs=1,
        help="Máximo de solicitudes a generar",
    )

    parser.add_argument(
        "--cant_por_prensa",
        metavar="cant_por_prensa",
        type=int,
        nargs=1,
        help="Cantidad máxima de jugadores por prensa",
    )

    parser.add_argument(
        "--step",
        metavar="step",
        type=int,
        nargs=1,
        help="Cantidad de solicitudes a incrementar en cada iteración",
    )

    args = parser.parse_args()

    if not args.direccion_salida:
        raise ValueError("Falta el argumento: direccion_salida")

    maximo = args.maximo[0] if args.maximo else 100
    cant_por_prensa = args.cant_por_prensa[0] if args.cant_por_prensa else 7
    direccion_salida = args.direccion_salida[0]
    step = args.step[0] if args.step else 10

    graficar_simulaciones(maximo, cant_por_prensa, direccion_salida, step)


if __name__ == "__main__":
    main()
