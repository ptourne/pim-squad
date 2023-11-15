from manejo_archivos import obtener_subconjuntos


def sol_por_greedy(subconjuntos):
    """
    Obtiene la solución por greedy.
    param subconjuntos: subconjuntos de jugadores pedidos por cada prensa
    return: solución
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
    for subconjunto in subconjuntos:
        subconjunto.sort(
            key=lambda jugador: apariciones[jugador], reverse=True)

    # obtenemos la solución mediante el óptimo local
    solucion = set()
    for subconjunto in subconjuntos:  # O(len(subconjuntos)*len(subconjunto))
        for jugador in subconjunto:
            if jugador in solucion:
                break
            solucion.add(jugador)
            break

    return solucion


def prueba_greedy():
    args = ["archivos_catedra/7.txt", "backtracking"]

    # subconjuntos = obtener_subconjuntos(args.archivo_entrada[0])
    # tipo_solucion = args.greedy_backtracking_lineal[0]

    subconjuntos = obtener_subconjuntos(args[0])

    for i in range(len(subconjuntos)):
        subconjuntos[i] = list(subconjuntos[i])

    solucion = sol_por_greedy(subconjuntos)
    print(str(solucion) + "\n")
