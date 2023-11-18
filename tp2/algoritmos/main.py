import argparse
import os
from manejo_archivos import esfuerzos_y_energias_archivo, exportar_resultado
from algoritmo import optimizar_entrenamiento


def main():
    parser = argparse.ArgumentParser(
        description="Determina qué entrenamientos maximizan la ganancia."
    )
    
    parser.add_argument(
        "archivo_entrada",
        metavar="n_esfuerzos_y_energias.txt",
        type=open,
        nargs=1,
        help="Archivo de entrada con el número de entrenamientos, los esfuerzos requeridos por cada entrenamiento y la energía disponible por cada día consecutivo de entrenamiento",
    )

    parser.add_argument(
        "-o",
        dest="archivo_salida",
        type=argparse.FileType("w", encoding="latin-1"),
        default="plan_entrenamiento_optimo.txt",
        help="Archivo de destino de la ganancia óptima y el plan de entreamiento que optimizan la ganancia",
    )

    args = parser.parse_args()

    archivo_entrada = args.archivo_entrada[0].name
    archivo_salida = args.archivo_salida.name

    n, esfuerzos, energias = esfuerzos_y_energias_archivo(archivo_entrada)

    nombre_archivo_entrada = os.path.basename(archivo_entrada)
    ganancia_maxima, plan_entrenamiento_optimo = optimizar_entrenamiento(
        n, esfuerzos, energias
    )
    
    exportar_resultado(
        archivo_salida,
        nombre_archivo_entrada,
        ganancia_maxima,
        plan_entrenamiento_optimo,
    )


if __name__ == "__main__":
    main()
