import argparse
from manejo_archivos import obtener_subconjuntos
from greedy import sol_por_greedy
from backtracking import bracktracking_hitting_set_problem
from programacion_lineal_entera import sol_por_prog_lineal


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

    args = ["archivos_catedra/200.txt", "lineal_entera"]

    # subconjuntos = obtener_subconjuntos(args.archivo_entrada[0])
    # tipo_solucion = args.greedy_backtracking_lineal[0]

    subconjuntos = obtener_subconjuntos(args[0])
    tipo_solucion = args[1]

    match tipo_solucion:
        case "greedy":
            solucion = sol_por_greedy(subconjuntos)
            print(solucion + "\n")
        case "backtracking":
            solucion = bracktracking_hitting_set_problem(subconjuntos)
            print(solucion + "\n")
        case "lineal_entera":
            solucion = sol_por_prog_lineal(subconjuntos)
            print(str(solucion) + "\n")
        case _:
            raise Exception("Algoritmo no reconocido")


if __name__ == "__main__":
    main()
