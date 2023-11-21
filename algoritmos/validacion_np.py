# O(n*m), siendo n la cantidad de subconjuntos y m la cantidad máxima de jugadores por subconjunto
def validar_solucion(b_array, sol_parcial):
    for i_b in range(len(b_array)):
        if not esta_incluido(b_array[i_b], sol_parcial):
            return False
    return True


def esta_incluido(b_array_set, sol_parcial):
    for jugador in b_array_set:
        if jugador in sol_parcial:
            return True
    return False
