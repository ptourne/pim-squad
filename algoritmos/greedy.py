def sol_por_greedy(subconjuntos):
    """
    Obtiene la solución por greedy.
    :param subconjuntos: subconjuntos de jugadores pedidos por cada prensa
    :return: solución
    """
    # contamos la cantidad de apariciones de cada jugador por cada prensa
    apariciones = {}
    for subconjunto in subconjuntos:  # O(len(subconjuntos)*len(subconjunto))
        for jugador in subconjunto:
            if jugador in apariciones:
                apariciones[jugador] += 1
            else:
                apariciones[jugador] = 1

    # ordenamos los subconjuntos por cantidad de apariciones de cada jugador de mayor a menor
    subconjuntos.sort(key=lambda pedido: max(
        [apariciones[jugador] for jugador in pedido]), reverse=True)

    # obtenemos la solución
    solucion = set()
    for subconjunto in subconjuntos:  # O(len(subconjuntos)*len(subconjunto))
        for jugador in subconjunto:
            if jugador in solucion:
                break
            solucion.add(jugador)
            break

    return solucion
