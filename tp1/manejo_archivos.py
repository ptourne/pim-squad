import csv
from algoritmos import Compilado


def compilados_en_archivo_a_lista(nombre_archivo):
    compilados = []

    with open(nombre_archivo, newline="") as archivo_tiempos:
        lector_csv = csv.reader(archivo_tiempos)
        next(lector_csv, None)
        for fila in lector_csv:
            compilados.append(Compilado(int(fila[0]), int(fila[1])))
    return compilados


def exportar_compilados(archivo_salida, compilados_ordenados):
    with open(archivo_salida, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["S_i", "A_i"])

        for compilado in compilados_ordenados:
            writer.writerow([compilado.tiempo_scaloni, compilado.tiempo_ayudante])
