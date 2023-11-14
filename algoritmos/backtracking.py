# Escribir un algoritmo que, por backtracking, obtenga la solución óptima al problema.
# Generar sets de datos para corroborar su correctitud, así como tomar mediciones de tiempos.

def backtracking_HSP(a, b_array, sol_parcial, sol_actual, i_b):
    if es_compatible(b_array, sol_parcial) & (len(sol_parcial) < len(sol_actual)):
        sol_actual = sol_parcial.copy()

    if len(sol_parcial) > len(sol_actual):
        return

    if i_b >= len(b_array):
        return

    if esta_incluido(b_array[i_b], sol_parcial):
        return backtracking_HSP(a, b_array, sol_parcial, sol_actual, i_b+1)

    for jugador in b_array[i_b]:
        sol_parcial.insert(jugador)
        backtracking_HSP(a, b_array, sol_parcial, sol_actual, i_b+1)
        sol_parcial.remove(jugador)


def es_compatible(b_array, sol_parcial):
    for i_b in range(len(b_array)):
        if not esta_incluido(b_array[i_b], sol_parcial):
            return False
    return True


def esta_incluido(b_array_set, sol_parcial):
    for jugador in b_array_set:
        if jugador in sol_parcial:
            return True
    return False


def bracktracking_hitting_set_problem(a, b_array):
    sol_parcial = []
    sol_actual = []
    i_b = 0
    backtracking_HSP(a, b_array, sol_parcial, sol_actual, i_b)
    return sol_actual
