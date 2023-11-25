import argparse
from generador_de_ejemplos import generar_ejemplos_abc
from manejo_archivos import obtener_subconjuntos
from backtracking import bracktracking_hitting_set_problem
from greedy import aproximacion_greedy_maximo_global_con_recalculo, aproximacion_greedy_maximo_por_grupos
from programacion_lineal_continua import hitting_set_pl_continua
from programacion_lineal_entera import hitting_set_pl_entera
from medicion_tiempo import tiempo_ejecucion_y_resultado


def comparar_soluciones(pedidos, archivo_salida):
    # tiempo_backtracking, sol_backtracking = tiempo_ejecucion_y_resultado(
    #     pedidos, bracktracking_hitting_set_problem)
    # tiempo_lineal_entera, sol_lineal_entera = tiempo_ejecucion_y_resultado(
    #     pedidos, hitting_set_pl_entera)
    tiempo_lineal_continua, sol_lineal_continua = tiempo_ejecucion_y_resultado(
        pedidos, hitting_set_pl_continua)
    tiempo_greedy, sol_greedy = tiempo_ejecucion_y_resultado(
        pedidos, aproximacion_greedy_maximo_global_con_recalculo)
    tiempo_greedy_maximo_por_grupos, sol_greedy_maximo_por_grupos = tiempo_ejecucion_y_resultado(
        pedidos, aproximacion_greedy_maximo_por_grupos)

    # Guardamos en un archivo los resultados
    with open(archivo_salida, 'w') as file:
        # file.write(
        #     f"Backtracking:\nCantidad mínima: {len(sol_backtracking)}\nSolución: {sol_backtracking}\nTiempo de ejecución: {tiempo_backtracking * 1000} milisegundos\n\n")
        # file.write(
        #     f"Programación Lineal Entera:\nCantidad mínima: {len(sol_lineal_entera)}\nSolución: {sol_lineal_entera}\nTiempo de ejecución: {tiempo_lineal_entera * 1000} milisegundos\n\n")
        file.write(
            f"Programación Lineal Continua:\nCantidad mínima: {len(sol_lineal_continua)}\nSolución: {sol_lineal_continua}\nTiempo de ejecución: {tiempo_lineal_continua * 1000} milisegundos\n\n")
        file.write(
            f"Greedy:\nCantidad mínima: {len(sol_greedy)}\nSolución: {sol_greedy}\nTiempo de ejecución: {tiempo_greedy * 1000} milisegundos\n\n")
        file.write(
            f"Greedy Máximo por Grupos:\nCantidad mínima: {len(sol_greedy_maximo_por_grupos)}\nSolución: {sol_greedy_maximo_por_grupos}\nTiempo de ejecución: {tiempo_greedy_maximo_por_grupos * 1000} milisegundos\n\n")


def main():
    # parser = argparse.ArgumentParser(
    #     description="Obtiene la solución al problema de hitting set problem"
    # )

    # parser.add_argument(
    #     "archivo_entrada",
    #     metavar="archivo",
    #     type=open,
    #     nargs=1,
    #     help="Archivo de entrada con los subconjuntos a utilizar",
    # )

    # parser.add_argument(
    #     "--direccion_salida",
    #     metavar="archivo",
    #     type=str,
    #     nargs=1,
    #     help="Dirección del archivo de salida con los resultados de la comparación",
    # )

    # args = parser.parse_args()

    # if not args.direccion_salida:
    #     raise ValueError("Falta el argumento: direccion_salida")

    # archivo_entrada = args.archivo_entrada[0].name
    # archivo_salida = args.direccion_salida[0] or "resultado_comparacion.txt"

    archivo_entrada = "../ejemplos/inmanejable/50000.txt"
    archivo_salida = "../resultados_comparaciones/inmanejable/50000.txt"

    subconjuntos = generar_ejemplos_abc(5000, 3, 10, 12, True, 25, True,)

    comparar_soluciones(subconjuntos, archivo_salida)


if __name__ == "__main__":
    main()
