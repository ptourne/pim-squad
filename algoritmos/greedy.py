from validacion_np import validar_solucion
from manejo_archivos import obtener_subconjuntos


def aproximacion_greedy(subconjuntos: list):
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

    # obtenemos la solución mediante el óptimo local
    solucion = set()
    for subconjunto in subconjuntos:  # O(len(subconjuntos)*len(subconjunto))
        solucion.add(max(subconjunto, key=lambda jugador: apariciones[jugador]))

    return solucion

def aproximacion_greedy_bis(subconjuntos: list):
    """
    Obtiene la solución por greedy.
    param subconjuntos: subconjuntos de jugadores pedidos por cada prensa
    return: solución
    """
    # contamos la cantidad de apariciones de cada jugador por cada prensa
    apariciones = {}
    for index, subconjunto in enumerate(subconjuntos): # O(len(subconjuntos)*len(subconjunto))
        for jugador in subconjunto:
            if jugador not in apariciones:
                apariciones[jugador] = set()
            apariciones[jugador].add(index)

    # obtenemos la solución mediante el óptimo local
    solucion = set()
    
    while len(apariciones) != 0:  # O(len(jugadores)*len(subconjuntos)*len(subconjunto))
        jugador , index_subconjuntos = max(apariciones.items(), key=lambda jugador_index_subconjuntos: len(jugador_index_subconjuntos[1]))
        apariciones.pop(jugador)
        if len(index_subconjuntos) == 0:
            break
        solucion.add(jugador)
        
        for index_subconjunto in index_subconjuntos:  # O(len(subconjuntos)*len(subconjunto))
            for jugador_compañero_de_conjunto in subconjuntos[index_subconjunto]:
                if jugador != jugador_compañero_de_conjunto:
                    apariciones[jugador_compañero_de_conjunto].remove(index_subconjunto)

    return solucion

def prueba_greedy():
    args = ["catedra_ejemplos/5.txt", "backtracking"]
    subconjuntos = obtener_subconjuntos(args[0])
    solucion_greedy = aproximacion_greedy(subconjuntos)
    solucion_greedy_bis = aproximacion_greedy_bis(subconjuntos)
    print("solucion_greedy:" + str(solucion_greedy))
    print("Len:" + str(len(solucion_greedy)))
    print("Es solución:" + str(validar_solucion(solucion_greedy, subconjuntos)))
    print("solucion_greedy_bis:" + str(solucion_greedy_bis))
    print("Len:" + str(len(solucion_greedy_bis)))
    print("Es solución:" + str(validar_solucion(solucion_greedy_bis, subconjuntos)) + "\n")
    args = ["catedra_ejemplos/7.txt", "backtracking"]
    subconjuntos = obtener_subconjuntos(args[0])
    solucion_greedy = aproximacion_greedy(subconjuntos)
    solucion_greedy_bis = aproximacion_greedy_bis(subconjuntos)
    print("solucion_greedy:" + str(solucion_greedy))
    print("Len:" + str(len(solucion_greedy)))
    print("Es solución:" + str(validar_solucion(solucion_greedy, subconjuntos)))
    print("solucion_greedy_bis:" + str(solucion_greedy_bis))
    print("Len:" + str(len(solucion_greedy_bis)))
    print("Es solución:" + str(validar_solucion(solucion_greedy_bis, subconjuntos)) + "\n")
    args = ["catedra_ejemplos/100.txt", "backtracking"]
    subconjuntos = obtener_subconjuntos(args[0])
    solucion_greedy = aproximacion_greedy(subconjuntos)
    solucion_greedy_bis = aproximacion_greedy_bis(subconjuntos)
    print("solucion_greedy:" + str(solucion_greedy))
    print("Len:" + str(len(solucion_greedy)))
    print("Es solución:" + str(validar_solucion(solucion_greedy, subconjuntos)))
    print("solucion_greedy_bis:" + str(solucion_greedy_bis))
    print("Len:" + str(len(solucion_greedy_bis)))
    print("Es solución:" + str(validar_solucion(solucion_greedy_bis, subconjuntos)) + "\n")

def main():
    prueba_greedy()

if __name__ == "__main__":
    main()
