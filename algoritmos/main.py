import argparse
from programacion_lineal_aprox import hitting_set_pl_continua
from manejo_archivos import obtener_subconjuntos
from greedy import aproximacion_greedy
from backtracking import bracktracking_hitting_set_problem
from programacion_lineal_entera import hitting_set_pl_entera


def main():
    # parser = argparse.ArgumentParser(
    #     description="Obtiene el menor conjunto de jugadores que cubre al menos un pedido de cada prensa"
    # )

    # parser.add_argument(
    #     "archivo_entrada",
    #     metavar="archivo con pedidos",
    #     type=open,
    #     nargs=1,
    #     help="Archivo de entrada con los pedidos de cada prensa",
    # )

    # parser.add_argument(
    #     "greedy_backtracking_lineal",
    #     metavar="algoritmo a elección",
    #     type=str,
    #     nargs=1,
    #     help="Algoritmo a utilizar para resolver el problema",
    # )

    # args = parser.parse_args()

    args = ["./nuestros_ejemplos/20.txt", "lineal_entera"]

    # subconjuntos = obtener_subconjuntos(args.archivo_entrada[0])
    # tipo_solucion = args.greedy_backtracking_lineal[0]

    subconjuntos = obtener_subconjuntos(args[0])
    tipo_solucion = args[1]

    match tipo_solucion:
        case "greedy":
            solucion = aproximacion_greedy(subconjuntos)
            print(solucion + "\n")

        case "backtracking":
            solucion = bracktracking_hitting_set_problem(subconjuntos)
            print(str(solucion) + "\n")

        case "lineal_entera":
            cant_jugadores, jugadores = hitting_set_pl_entera(
                subconjuntos)
            print("cant_jugadores: " + str(cant_jugadores) + "\n" + "-----" +
                  "jugadores: " + str(jugadores) + "\n")

        case "lineal_continua":
            cant_jugadores, jugadores = hitting_set_pl_continua(
                subconjuntos)
            print("cant_jugadores: " + str(cant_jugadores) + "\n" + "-----" +
                  "jugadores: " + str(jugadores) + "\n")

        case _:
            raise Exception("Algoritmo no reconocido")


if __name__ == "__main__":
    main()
