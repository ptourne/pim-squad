from algoritmos.manejo_archivos import obtener_subconjuntos
from algoritmos.backtracking import bracktracking_hitting_set_problem
from algoritmos.greedy import aproximacion_greedy_bis
from medicion_tiempo import tiempo_ejecucion_y_resultado
from nuestros_ejemplos.generador_de_ejemplos import generar_ejemplos
from algoritmos.programacion_lineal_continua import hitting_set_pl_continua
from algoritmos.programacion_lineal_entera import hitting_set_pl_entera


def comparar_soluciones(pedidos):
    tiempo_backtracking, sol_backtracking = tiempo_ejecucion_y_resultado(
        pedidos, bracktracking_hitting_set_problem)
    tiempo_lineal_entera, sol_lineal_entera = tiempo_ejecucion_y_resultado(
        pedidos, hitting_set_pl_entera)
    tiempo_lineal_continua, sol_lineal_continua = tiempo_ejecucion_y_resultado(
        pedidos, hitting_set_pl_continua)
    tiempo_greedy, sol_greedy = tiempo_ejecucion_y_resultado(
        pedidos, aproximacion_greedy_bis)

    # Guardamos en un archivo los resultados
    with open('resultados.txt', 'w') as file:
        file.write(
            f"Backtracking:\n{sol_backtracking}\n{tiempo_backtracking}\n\n")
        file.write(
            f"Programación Lineal Entera:\n{sol_lineal_entera}\n{tiempo_lineal_entera}\n\n")
        file.write(
            f"Programación Lineal Continua:\n{sol_lineal_continua}\n{tiempo_lineal_continua}\n\n")
        file.write(f"Greedy:\n{sol_greedy}\n{tiempo_greedy}\n\n")


pedidos = obtener_subconjuntos("../nuestros_ejemplos/5_muchos.txt")
comparar_soluciones(pedidos)
