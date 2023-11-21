from manejo_archivos import obtener_subconjuntos
from backtracking import bracktracking_hitting_set_problem
from greedy import aproximacion_greedy_maximo_global_con_recalculo
from medicion_tiempo import tiempo_ejecucion_y_resultado
from programacion_lineal_continua import hitting_set_pl_continua
from programacion_lineal_entera import hitting_set_pl_entera


def comparar_soluciones(pedidos, archivo_salida="resultados.txt"):
    tiempo_backtracking, sol_backtracking = tiempo_ejecucion_y_resultado(
        pedidos, bracktracking_hitting_set_problem)
    tiempo_lineal_entera, sol_lineal_entera = tiempo_ejecucion_y_resultado(
        pedidos, hitting_set_pl_entera)
    tiempo_lineal_continua, sol_lineal_continua = tiempo_ejecucion_y_resultado(
        pedidos, hitting_set_pl_continua)
    tiempo_greedy, sol_greedy = tiempo_ejecucion_y_resultado(
        pedidos, aproximacion_greedy_maximo_global_con_recalculo)

    # Guardamos en un archivo los resultados
    with open(archivo_salida, 'w') as file:
        file.write(
            f"Backtracking:\nSolución: {sol_backtracking}\nTiempo de ejecución: {tiempo_backtracking * 1000} milisegundos\n\n")
        file.write(
            f"Programación Lineal Entera:\nSolución: {sol_lineal_entera}\nTiempo de ejecución: {tiempo_lineal_entera * 1000} milisegundos\n\n")
        file.write(
            f"Programación Lineal Continua:\nSolución: {sol_lineal_continua}\nTiempo de ejecución: {tiempo_lineal_continua * 1000} milisegundos\n\n")
        file.write(
            f"Greedy:\nSolución: {sol_greedy}\nTiempo de ejecución: {tiempo_greedy * 1000} milisegundos\n\n")


pedidos = obtener_subconjuntos("../ejemplos/catedra/20.txt")
comparar_soluciones(pedidos, "../resultados_comparaciones/catedra/20.txt")
