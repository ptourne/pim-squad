import argparse
from logging import raiseExceptions
from programacion_lineal_continua import hitting_set_pl_continua
from manejo_archivos import obtener_subconjuntos
from greedy import aproximacion_greedy_maximo_global_con_recalculo
from backtracking import bracktracking_hitting_set_problem
from programacion_lineal_entera import hitting_set_pl_entera


def main():
    parser = argparse.ArgumentParser(
        description="Obtiene la solución al problema de hitting set problem"
    )

    parser.add_argument(
        "archivo_entrada",
        metavar="archivo con subconjuntos",
        type=open,
        nargs='?',
        help="Archivo de entrada con los subconjuntos a utilizar",
    )

    parser.add_argument(
        "greedy_backtracking_lineal",
        metavar="algoritmo a elección\n greedy - backtracking - lineal_entera - lineal_continua",
        type=str,
        nargs='?',
        help="Algoritmo a utilizar para resolver el problema\ngreedy - backtracking - lineal_entera - lineal_continua",
    )

    args = parser.parse_args()

    if not args.greedy_backtracking_lineal:
        raise Exception("Falta el algoritmo a utilizar")

    archivo_entrada = args.archivo_entrada.name if args.archivo_entrada else raiseExceptions(
        "Falta el archivo de entrada")
    subconjuntos = obtener_subconjuntos(archivo_entrada)

    tipo_solucion = args.greedy_backtracking_lineal

    solucion = "La solución por " + tipo_solucion + " es: \n"
    match tipo_solucion:
        case "greedy":
            solucion_greedy = aproximacion_greedy_maximo_global_con_recalculo(
                subconjuntos)
            solucion += str(solucion_greedy) + "\n"

        case "backtracking":
            solucion_bracktracking = bracktracking_hitting_set_problem(
                subconjuntos)
            solucion += str(solucion_bracktracking) + "\n"

        case "lineal_entera":
            solucion_pl_entera = hitting_set_pl_entera(
                subconjuntos)
            solucion += str(solucion_pl_entera) + "\n"

        case "lineal_continua":
            solucion_pl_continua = hitting_set_pl_continua(
                subconjuntos)
            solucion += str(solucion_pl_continua) + "\n"

        case _:
            raise Exception("Algoritmo no reconocido")

    print(solucion)
    return solucion


if __name__ == "__main__":
    main()
