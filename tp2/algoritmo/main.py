import argparse

from manejo_archivos import esfuerzos_y_energias_archivo
from algoritmo import compilados_ordenados_de_forma_optima


def main():
    parser = argparse.ArgumentParser(
        description="Determina qué entrenamientos maximizan la ganancia."
    )
    parser.add_argument(
        "archivo_entrada",
        metavar="n_esfuerzos_y_energias.csv",
        type=open,
        nargs=1,
        help='Archivo de entrada con el número de entrenamientos, los esfuerzos requeridos por cada entrenamiento y la energía disponible por cada día consecutivo de entrenamiento',
    )

    parser.add_argument(
        "-o",
        dest="archivo_salida",
        type=argparse.FileType("w", encoding="latin-1"),
        default="Entrenamientos a elegir",
        help="Archivos de destino de la ganancia óptima y los entreamientos que optimizan la ganancia",
    )

    args = parser.parse_args()

    archivo_entrada = args.archivo_entrada[0].name
    archivo_salida = args.archivo_salida.name

    compilados = (archivo_entrada)
    compilados_ordenados = compilados_ordenados_de_forma_optima(compilados)

    # exportar_compilados(archivo_salida, compilados_ordenados)


if __name__ == "__main__":
    main()