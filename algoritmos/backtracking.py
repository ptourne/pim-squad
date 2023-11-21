# Escribir un algoritmo que, por backtracking, obtenga la solución óptima al problema.
# Generar sets de datos para corroborar su correctitud, así como tomar mediciones de tiempos.

def backtracking_HSP(b_array: list, sol_parcial: set, sol_actual, i_b):
    if i_b >= len(b_array):
        if sol_actual == None or len(sol_parcial) < len(sol_actual):
            return sol_parcial.copy()
        return sol_actual

    if sol_actual != None and len(sol_parcial) >= len(sol_actual):
        return sol_actual

    if esta_incluido(b_array[i_b], sol_parcial):
        return backtracking_HSP(b_array, sol_parcial, sol_actual, i_b+1)

    for jugador in b_array[i_b]:
        sol_parcial.add(jugador)
        sol_actual = backtracking_HSP(b_array, sol_parcial, sol_actual, i_b+1)
        sol_parcial.remove(jugador)

    return sol_actual


def esta_incluido(b_array_set, sol_parcial):
    for jugador in b_array_set:
        if jugador in sol_parcial:
            return True
    return False


def bracktracking_hitting_set_problem(b_array):
    sol_parcial = set()
    sol_actual = None
    i_b = 0
    sol_actual = backtracking_HSP(b_array, sol_parcial, sol_actual, i_b)
    return sol_actual
