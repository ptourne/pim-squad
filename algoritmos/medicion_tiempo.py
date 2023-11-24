import argparse
import time

import numpy as np
import matplotlib.pyplot as plt
from backtracking import bracktracking_hitting_set_problem
from greedy import aproximacion_greedy_maximo_por_grupos, aproximacion_greedy_maximo_global_con_recalculo
from programacion_lineal_continua import hitting_set_pl_continua
from programacion_lineal_entera import hitting_set_pl_entera
from generador_de_ejemplos import generar_ejemplos_abc


def tiempo_ejecucion_y_resultado(solicitudes, algoritmo):
    tiempo_inicial = time.process_time()
    resultado = algoritmo(solicitudes)
    tiempo_final = time.process_time()
    return tiempo_final - tiempo_inicial, resultado


def graficar_simulaciones(maximo=10, cant_por_conjunto=4, path_salida="medicion_prueba", step=1):
    mediciones_back = []
    mediciones_lin_ent = []
    mediciones_lin_cont = []
    mediciones_greedy_maximo_por_grupos = []
    mediciones_greedy_global_con_recalculo = []

    # Generamos las mediciones de tiempo por cada generación de ejemplo
    for i in range(1, maximo+2, step):
        cant_minima = min(i, cant_por_conjunto)
        suma_provisoria_greedy_maximo_por_grupos = 0
        suma_provisoria_greedy_global_con_recalculo = 0
        suma_provisoria_prog_lineal_cont = 0
        suma_provisoria_prog_lineal_ent = 0
        aprox_greedy1 = []
        aprox_greedy2 = []
        aprox_prog_lineal_cont = []

        for _ in range(10):
            solicitudes = generar_ejemplos_abc(
                i, 2, cant_minima, i, True, i)
            for _ in range(2):
                tiempo, solucion_optima = tiempo_ejecucion_y_resultado(
                    solicitudes, hitting_set_pl_entera)
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
                    solicitudes, hitting_set_pl_continua)
                suma_provisoria_prog_lineal_cont += tiempo

                aprox_greedy1.append(
                    len(solucion_greedy1)/len(solucion_optima))
                aprox_greedy2.append(
                    len(solucion_greedy2)/len(solucion_optima))
                aprox_prog_lineal_cont.append(
                    len(solucion_greedy2)/len(solucion_optima))

        aprox_greedy1 = sum(aprox_greedy1)/len(aprox_greedy1)
        aprox_greedy2 = sum(aprox_greedy2)/len(aprox_greedy2)
        aprox_prog_lineal_cont = sum(aprox_prog_lineal_cont)/len(
            aprox_prog_lineal_cont
        )

        mediciones_greedy_maximo_por_grupos.append(
            (i, suma_provisoria_greedy_maximo_por_grupos/20, aprox_greedy1))
        mediciones_greedy_global_con_recalculo.append(
            (i, suma_provisoria_greedy_global_con_recalculo/20, aprox_greedy2))
        mediciones_lin_cont.append(
            (i, suma_provisoria_prog_lineal_cont/20, aprox_prog_lineal_cont))
        mediciones_lin_ent.append(
            (i, suma_provisoria_prog_lineal_ent/20, aprox_prog_lineal_cont))

        # tiempo, _ = tiempo_ejecucion_y_resultado(
        #     solicitudes, bracktracking_hitting_set_problem
        # )
        # mediciones_back.append((i, tiempo))

    # Separamos los valores de x e y
    x_back = [medicion[0] for medicion in mediciones_back]
    y_back = [medicion[1] for medicion in mediciones_back]

    x_lin_ent = [medicion[0] for medicion in mediciones_lin_ent]
    y_lin_ent = [medicion[1] for medicion in mediciones_lin_ent]

    x_lin_cont = [medicion[0] for medicion in mediciones_lin_cont]
    y_lin_cont = [medicion[1] for medicion in mediciones_lin_cont]
    aprox_prog_lineal_cont = [medicion[2]
                              for medicion in mediciones_lin_cont]

    x_greedy_maximo_por_grupos = [medicion[0]
                                  for medicion in mediciones_greedy_maximo_por_grupos]
    y_greedy_maximo_por_grupos = [medicion[1]
                                  for medicion in mediciones_greedy_maximo_por_grupos]
    aprox_greedy_maximo_por_grupos = [medicion[2]
                                      for medicion in mediciones_greedy_maximo_por_grupos]

    x_greedy_global_con_recalculo = [medicion[0]
                                     for medicion in mediciones_greedy_global_con_recalculo]
    y_greedy_global_con_recalculo = [medicion[1]
                                     for medicion in mediciones_greedy_global_con_recalculo]
    aprox_greedy_global_con_recalculo = [medicion[2]
                                         for medicion in mediciones_greedy_global_con_recalculo]

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
    plt.figure()

    plt.scatter(x_greedy_maximo_por_grupos,
                y_greedy_maximo_por_grupos, label="Greedy por máximos", color='purple')
    plt.scatter(x_greedy_global_con_recalculo,
                y_greedy_global_con_recalculo, label="Greedy por cálculos", color='orange')

    # Configurar el gráfico
    plt.xlabel("Cantidad de solicitudes")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución de los algoritmos")
    plt.legend()

    # Guardar el gráfico
    plt.savefig(path_salida)

    ########################################################

    # Configuramos nuestra programación lineal
    plt.figure()

    plt.scatter(x_lin_ent, y_lin_ent,
                label="Programación Lineal Entera", color='green')
    plt.scatter(x_lin_cont, y_lin_cont,
                label="Programación Lineal Continua", color='blue')

    # Configurar el gráfico
    plt.xlabel("Cantidad de solicitudes")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución de los algoritmos")
    plt.legend()

    # Guardar el gráfico
    plt.savefig(path_salida + "_lin")

    ########################################################

    # Configuramos nuestra aproximación por programación lineal
    plt.figure()

    plt.scatter(x_lin_cont, aprox_prog_lineal_cont,
                label="Aproximación Programación Lineal Continua", color='blue')

    # Configurar el gráfico
    plt.xlabel("Cantidad de solicitudes")
    plt.ylabel("Aproximación Lineal Continua")
    plt.title("Aproximación de la Programación Lineal Continua")
    plt.legend()

    # Guardar el gráfico
    plt.savefig(path_salida + "_aprox_lin")

    ########################################################

    plt.figure()
    plt.scatter(x_greedy_maximo_por_grupos,
                aprox_greedy_maximo_por_grupos, label="Aproximación greedy Máximo por Grupos", color='purple')
    plt.scatter(x_greedy_global_con_recalculo,
                aprox_greedy_global_con_recalculo, label="Aproximación greedy Global con Recálculo", color='orange')

    # Configurar el gráfico
    plt.xlabel("Cantidad de solicitudes")
    plt.ylabel("Aproximación")
    plt.title("Aproximación de los algoritmos Greedy")
    plt.legend()

    # Guardar el gráfico
    plt.savefig(path_salida + "_aprox")


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
