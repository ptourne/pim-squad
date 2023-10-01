import csv

def esfuerzos_y_energias_archivo(nombre_archivo):
    filas = []

    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            filas.append(int(linea.strip()))

    n = filas[0]
    esfuerzos = filas[1:n+1]
    energias = filas[n+1:]
    return n, esfuerzos, energias


# def exportar_compilados(archivo_salida, compilados_ordenados):
#     with open(archivo_salida, "w", newline="") as file:
#         writer = csv.writer(file)

#         writer.writerow(["S_i", "A_i"])

#         for compilado in compilados_ordenados:
#             writer.writerow([compilado.tiempo_scaloni, compilado.tiempo_ayudante])