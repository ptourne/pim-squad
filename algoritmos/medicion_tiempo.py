import argparse
import time

import numpy as np
import matplotlib.pyplot as plt
from backtracking import bracktracking_hitting_set_problem
from greedy import (
    aproximacion_greedy_maximo_por_grupos,
    aproximacion_greedy_maximo_global_con_recalculo,
)
from programacion_lineal_continua import hitting_set_pl_continua
from programacion_lineal_entera import hitting_set_pl_entera
from generador_de_ejemplos import generar_ejemplos_abc


def tiempo_ejecucion_y_resultado(solicitudes, algoritmo):
    tiempo_inicial = time.process_time()
    resultado = algoritmo(solicitudes)
    tiempo_final = time.process_time()
    return tiempo_final - tiempo_inicial, resultado


def graficar_simulaciones(
    maximo,
    cant_max_por_subconjunto,
    cant_min_por_subconjunto,
    path_salida,
    step,
):
    mediciones_back = []
    mediciones_lin_ent = []
    mediciones_lin_cont = []
    mediciones_greedy_maximo_por_grupos = []
    mediciones_greedy_global_con_recalculo = []
    aprox_greedy_maximo_por_grupos = []
    aprox_greedy_global_con_recalculo = []
    aprox_prog_lineal_cont = []

    # Generamos las mediciones de tiempo por cada generación de ejemplo
    for i in range(1, maximo + 2, step):
        print("Paso " + str(i) + " de " + str(maximo+1))
        cant_minima = min(i, cant_min_por_subconjunto)
        suma_provisoria_greedy_maximo_por_grupos = 0
        suma_provisoria_greedy_global_con_recalculo = 0
        suma_provisoria_prog_lineal_cont = 0
        suma_provisoria_prog_lineal_ent = 0
        suma_provisoria_back = 0

        for _ in range(5):
            aprox_greedy1_temp = int()
            aprox_greedy2_temp = int()
            aprox_prog_lineal_cont_temp = int()

            solicitudes = generar_ejemplos_abc(
                i, 2, cant_minima, cant_max_por_subconjunto, True, i
            )
            for _ in range(2):
                tiempo, solucion_optima = tiempo_ejecucion_y_resultado(
                    solicitudes, hitting_set_pl_entera
                )
                suma_provisoria_prog_lineal_ent += tiempo

                tiempo, solucion_greedy1 = tiempo_ejecucion_y_resultado(
                    solicitudes, aproximacion_greedy_maximo_por_grupos
                )
                suma_provisoria_greedy_maximo_por_grupos += tiempo

                tiempo, solucion_greedy2 = tiempo_ejecucion_y_resultado(
                    solicitudes, aproximacion_greedy_maximo_global_con_recalculo
                )
                suma_provisoria_greedy_global_con_recalculo += tiempo

                tiempo, _ = tiempo_ejecucion_y_resultado(
                    solicitudes, hitting_set_pl_continua
                )
                suma_provisoria_prog_lineal_cont += tiempo

                # tiempo, _ = tiempo_ejecucion_y_resultado(
                #     solicitudes, bracktracking_hitting_set_problem
                # )
                # suma_provisoria_back += tiempo

                aprox_greedy1_temp = len(
                    solucion_greedy1) / len(solucion_optima)
                aprox_greedy2_temp = len(
                    solucion_greedy2) / len(solucion_optima)
                aprox_prog_lineal_cont_temp = len(
                    solucion_optima) / len(solucion_optima)

            aprox_greedy_maximo_por_grupos.append((i, aprox_greedy1_temp))
            aprox_greedy_global_con_recalculo.append(
                (i, aprox_greedy2_temp))
            aprox_prog_lineal_cont.append((i, aprox_prog_lineal_cont_temp))

        mediciones_greedy_maximo_por_grupos.append(
            (i, suma_provisoria_greedy_maximo_por_grupos / 10)
        )
        mediciones_greedy_global_con_recalculo.append(
            (i, suma_provisoria_greedy_global_con_recalculo / 10)
        )
        mediciones_lin_cont.append(
            (i, suma_provisoria_prog_lineal_cont / 10)
        )
        mediciones_lin_ent.append((i, suma_provisoria_prog_lineal_ent / 10))
        mediciones_back.append((i, suma_provisoria_back / 10))

    # Separamos los valores de x e y
    x_back = [medicion[0] for medicion in mediciones_back]
    y_back = [medicion[1] for medicion in mediciones_back]

    x_lin_ent = [medicion[0] for medicion in mediciones_lin_ent]
    y_lin_ent = [medicion[1] for medicion in mediciones_lin_ent]

    x_lin_cont = [medicion[0] for medicion in mediciones_lin_cont]
    y_lin_cont = [medicion[1] for medicion in mediciones_lin_cont]

    x_greedy_maximo_por_grupos = [
        medicion[0] for medicion in mediciones_greedy_maximo_por_grupos
    ]
    y_greedy_maximo_por_grupos = [
        medicion[1] for medicion in mediciones_greedy_maximo_por_grupos
    ]

    x_greedy_global_con_recalculo = [
        medicion[0] for medicion in mediciones_greedy_global_con_recalculo
    ]
    y_greedy_global_con_recalculo = [
        medicion[1] for medicion in mediciones_greedy_global_con_recalculo
    ]

    # Exportamos los gráficos
    exportar_grafico_puntos(
        x_back,
        y_back,
        x_lin_ent,
        y_lin_ent,
        x_lin_cont,
        y_lin_cont,
        aprox_prog_lineal_cont,
        x_greedy_maximo_por_grupos,
        y_greedy_maximo_por_grupos,
        aprox_greedy_maximo_por_grupos,
        x_greedy_global_con_recalculo,
        y_greedy_global_con_recalculo,
        aprox_greedy_global_con_recalculo,
        path_salida,
    )


def exportar_grafico_puntos(
    x_back,
    y_back,
    x_lin_ent,
    y_lin_ent,
    x_lin_cont,
    y_lin_cont,
    aprox_prog_lineal_cont,
    x_greedy_maximo_por_grupos,
    y_greedy_maximo_por_grupos,
    aprox_greedy_maximo_por_grupos,
    x_greedy_global_con_recalculo,
    y_greedy_global_con_recalculo,
    aprox_greedy_global_con_recalculo,
    path_salida,
):
    # Configuramos nuestros tiempos de Greedy
    plt.figure()

    plt.scatter(
        x_greedy_maximo_por_grupos,
        y_greedy_maximo_por_grupos,
        label="Greedy por máximos",
        color="purple",
    )
    plt.scatter(
        x_greedy_global_con_recalculo,
        y_greedy_global_con_recalculo,
        label="Greedy por cálculos",
        color="orange",
    )

    # Configurar el gráfico
    plt.xlabel("Cantidad de solicitudes")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title(
        "Tiempo de ejecución de los algoritmos Greedy variando la cantidad de subconjuntos")
    plt.legend()

    # Guardar el gráfico
    plt.savefig(path_salida + "_tiempos_greedy_variando_n")

    ########################################################

    # Configuramos nuestros tiempos de programación lineal
    plt.figure()

    plt.scatter(x_lin_ent, y_lin_ent,
                label="Programación Lineal Entera", color="green")
    plt.scatter(
        x_lin_cont, y_lin_cont, label="Programación Lineal Continua", color="blue"
    )

    # Configurar el gráfico
    plt.xlabel("Cantidad de solicitudes")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title(
        "Tiempo de ejecución de los algoritmos de Programación Lineal variando la cantidad de subconjuntos")
    plt.legend()

    # Guardar el gráfico
    plt.savefig(path_salida + "_tiempos_lineal_variando_n")

    ########################################################

    # # Configuramos nuestros tiempos de backtracking
    # plt.figure()

    # plt.scatter(x_back, y_back, label="Backtracking", color='red')

    # # Configurar el gráfico
    # plt.xlabel("Cantidad de solicitudes")
    # plt.ylabel("Tiempo de ejecución (segundos)")
    # plt.title("Tiempo de ejecución de los algoritmos")
    # plt.legend()

    # # Guardar el gráfico
    # plt.savefig(path_salida + "_tiempos_back")

    ########################################################

    # Configuramos nuestra aproximación por programación lineal
    plt.figure()

    x_lineal = []
    y_lineal = []
    for (x, y) in aprox_prog_lineal_cont:
        x_lineal.append(x)
        y_lineal.append(y)
    plt.scatter(x_lineal, y_lineal, color='blue', alpha=0.5,
                label='Aproximación Lineal Continua')

    # Configurar el gráfico
    plt.xlabel("Cantidad de solicitudes")
    plt.ylabel("Aproximación Lineal Continua")
    plt.title(
        "Aproximación de la Programación Lineal Continua variando la cantidad de subconjuntos")
    plt.legend()

    # Guardar el gráfico
    plt.savefig(path_salida + "_aprox_lin_variando_n")

    ########################################################

    # Configuramos nuestra aproximación por greedy
    plt.figure()

    x_greedy1 = []
    y_greedy1 = []
    for (x, y) in aprox_greedy_maximo_por_grupos:
        x_greedy1.append(x)
        y_greedy1.append(y)
    plt.scatter(x_greedy1, y_greedy1, color="purple", alpha=0.5,
                label="Aproximación Greedy por máximos")

    x_greedy2 = []
    y_greedy2 = []
    for (x, y) in aprox_greedy_global_con_recalculo:
        x_greedy2.append(x)
        y_greedy2.append(y)
    plt.scatter(x_greedy2, y_greedy2, color="orange", alpha=0.5,
                label="Aproximación Greedy por cálculos")

    # Configurar el gráfico
    plt.xlabel("Cantidad de solicitudes")
    plt.ylabel("Aproximación")
    plt.title("Aproximación de los algoritmos Greedy variando la cantidad de subconjuntos")
    plt.legend()

    # Guardar el gráfico
    plt.savefig(path_salida + "_aprox_greedy_variando_n")


def main():
    parser = argparse.ArgumentParser(
        description="Guarda en un archivo un gráfico con los tiempos de ejecución de los algoritmos"
    )

    parser.add_argument(
        "direccion_salida",
        metavar="archivo",
        type=str,
        nargs=1,
        help="Dirección del archivo de salida (sin extensión) que contendrá cada gráfico",
    )

    parser.add_argument(
        "--maximo_del_grafico",
        metavar="maximo",
        type=int,
        nargs=1,
        help="Máximo de subconjuntos a generar para los gráficos",
    )

    parser.add_argument(
        "--cant_max_por_prensa",
        metavar="cant_max_por_prensa",
        type=int,
        nargs=1,
        help="Cantidad máxima de jugadores por prensa",
    )

    parser.add_argument(
        "--cant_min_por_prensa",
        metavar="cant_min_por_prensa",
        type=int,
        nargs=1,
        help="Cantidad mínima de jugadores por prensa",
    )

    parser.add_argument(
        "--step",
        metavar="step",
        type=int,
        nargs=1,
        help="Cantidad de subconjuntos a incrementar por cada gráfico",
    )

    args = parser.parse_args()

    if not args.direccion_salida:
        raise ValueError("Falta el argumento: direccion_salida")

    cant_max_por_prensa = (
        args.cant_max_por_prensa[0] if args.cant_max_por_prensa else 30
    )
    cant_min_por_prensa = (
        args.cant_min_por_prensa[0] if args.cant_min_por_prensa else 25
    )
    maximo_del_grafico = args.maximo_del_grafico[0] if args.maximo_del_grafico else 50
    direccion_salida = args.direccion_salida[0]
    step = args.step[0] if args.step else 10

    if cant_min_por_prensa > cant_max_por_prensa:
        raise ValueError(
            "La cantidad mínima de jugadores por prensa no puede ser mayor a la cantidad máxima"
        )

    if step < 1:
        raise ValueError("El step debe ser mayor a 0")

    graficar_simulaciones(
        maximo_del_grafico,
        cant_max_por_prensa,
        cant_min_por_prensa,
        direccion_salida,
        step,
    )


if __name__ == "__main__":
    main()
