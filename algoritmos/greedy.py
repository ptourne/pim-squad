from validacion_np import validar_solucion
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

    for i in range(len(subconjuntos)):
        subconjunto_i = list(subconjuntos[i])
        subconjunto_i.sort(
            key=lambda jugador: apariciones[jugador], reverse=True)
        subconjuntos[i] = subconjunto_i

    # obtenemos la solución mediante el óptimo local
    solucion = set()
    for subconjunto in subconjuntos:  # O(len(subconjuntos)*len(subconjunto))
        solucion.add(subconjunto[0])

    return solucion

def sol_por_greedy_bis(subconjuntos):
    """
    Obtiene la solución por greedy.
    param subconjuntos: subconjuntos de jugadores pedidos por cada prensa
    return: solución
    """
    # contamos la cantidad de apariciones de cada jugador por cada prensa
    apariciones = {}
    jugadores = []
    for subconjunto in subconjuntos:  # O(len(subconjuntos)*len(subconjunto))
        for jugador_compañero_de_conjunto in subconjunto:
            if jugador_compañero_de_conjunto not in apariciones:
                apariciones[jugador_compañero_de_conjunto] = set()
                jugadores.append(jugador_compañero_de_conjunto)
            apariciones[jugador_compañero_de_conjunto].add(tuple(subconjunto))

    # ordenamos los subconjuntos por cantidad de apariciones de cada jugador
    jugadores.sort(
            key=lambda jugador: len(apariciones[jugador]))
    
    # obtenemos la solución mediante el óptimo local
    solucion = set()
    
    while len(jugadores) != 0:  # O(len(jugadores)*len(subconjuntos)*len(subconjunto))
        jugador = jugadores.pop()
        apariciones_jugador = apariciones[jugador]
        if len(apariciones_jugador) == 0:
            break
        solucion.add(jugador)
        
        for subconjunto in set(apariciones_jugador):  # O(len(subconjuntos)*len(subconjunto))
            for jugador_compañero_de_conjunto in subconjunto:
                apariciones[jugador_compañero_de_conjunto].remove(subconjunto)
        
        jugadores.sort(
            key=lambda jugador: len(apariciones[jugador]))

    return solucion

def prueba_greedy():
    args = ["catedra_ejemplos/5.txt", "backtracking"]
    subconjuntos = obtener_subconjuntos(args[0])
    solucion_greedy = sol_por_greedy(subconjuntos)
    solucion_greedy_bis = sol_por_greedy_bis(subconjuntos)
    print("solucion_greedy:" + str(solucion_greedy))
    print("Es solución:" + str(validar_solucion(solucion_greedy, subconjuntos)))
    print("solucion_greedy_bis:" + str(solucion_greedy_bis))
    print("Es solución:" + str(validar_solucion(solucion_greedy_bis, subconjuntos)) + "\n")

def main():
    prueba_greedy()

if __name__ == "__main__":
    main()
