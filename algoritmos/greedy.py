def aproximacion_greedy_maximo_por_grupos(subconjuntos: list):
    """
    Obtiene la solucion por greedy.
    param subconjuntos: subconjuntos de jugadores pedidos por cada prensa
    return: solucion
    """
    # contamos la cantidad de apariciones de cada jugador por cada prensa
    apariciones = {}
    for subconjunto in subconjuntos:  # O(len(subconjuntos)*len(subconjunto))
        for jugador in subconjunto:
            if jugador in apariciones:
                apariciones[jugador] += 1
            else:
                apariciones[jugador] = 1

    # ordenamos los subconjuntos por cantidad de apariciones de cada jugador

    # obtenemos la solucion mediante el optimo local
    solucion = set()
    for subconjunto in subconjuntos:  # O(len(subconjuntos)*len(subconjunto))
        aparicion_max = None
        for jugador in subconjunto:
            if jugador in solucion:
                aparicion_max = jugador
                break

            else:
                if aparicion_max is None or apariciones[jugador] > apariciones[aparicion_max]:
                    aparicion_max = jugador

        solucion.add(aparicion_max)

    return solucion

def aproximacion_greedy_maximo_global_con_recalculo(subconjuntos: list):
    """
    Obtiene la solucion por greedy.
    param subconjuntos: subconjuntos de jugadores pedidos por cada prensa
    return: solucion
    """
    # contamos la cantidad de apariciones de cada jugador por cada prensa
    apariciones = {}
    # O(len(subconjuntos)*len(subconjunto))
    for index, subconjunto in enumerate(subconjuntos):
        for jugador in subconjunto:
            if jugador not in apariciones:
                apariciones[jugador] = set()
            apariciones[jugador].add(index)

    # obtenemos la solucion mediante el optimo local
    solucion = set()

    while len(apariciones) != 0:  # O(len(jugadores)*len(subconjuntos)*len(subconjunto))
        jugador, index_subconjuntos = max(apariciones.items(
        ), key=lambda jugador_index_subconjuntos: len(jugador_index_subconjuntos[1]))
        apariciones.pop(jugador)
        if len(index_subconjuntos) == 0:
            break
        solucion.add(jugador)

        # O(len(subconjuntos)*len(subconjunto))
        for index_subconjunto in index_subconjuntos:
            for jugador_companiero_de_conjunto in subconjuntos[index_subconjunto]:
                if jugador != jugador_companiero_de_conjunto:
                    apariciones[jugador_companiero_de_conjunto].remove(
                        index_subconjunto)

    return solucion
