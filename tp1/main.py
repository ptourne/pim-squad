import argparse

from manejo_archivos import compilados_en_archivo_a_lista, exportar_compilados
from algoritmos import compilados_ordenados_de_forma_optima


def main():
    parser = argparse.ArgumentParser(
        description="Ordena los compilados de manera que se minimice el tiempo total de análisis."
    )
    parser.add_argument(
        "archivo_entrada",
        metavar="compilados_a_ordenar.csv",
        type=open,
        nargs=1,
        help='Archivo .csv de entrada con el encabezado "S_i,A_i"',
    )

    parser.add_argument(
        "-o",
        dest="archivo_salida",
        type=argparse.FileType("w", encoding="latin-1"),
        default="compilados_ordenados.csv",
        help="Archivos de destino de los compilados ordenados def forma óptima",
    )

    args = parser.parse_args()

    archivo_entrada = args.archivo_entrada[0].name
    archivo_salida = args.archivo_salida.name

    compilados = compilados_en_archivo_a_lista(archivo_entrada)
    compilados_ordenados = compilados_ordenados_de_forma_optima(compilados)

    exportar_compilados(archivo_salida, compilados_ordenados)


if __name__ == "__main__":
    main()
