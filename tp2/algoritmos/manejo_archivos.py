def esfuerzos_y_energias_archivo(nombre_archivo):
    filas = []

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            filas.append(int(linea.strip()))

    n = filas[0]
    esfuerzos = filas[1 : n + 1]
    energias = filas[n + 1 :]
    return n, esfuerzos, energias


def exportar_resultado(
    archivo_salida, archivo_entrada, ganancia_maxima, plan_entrenamiento_optimo
):
    with open(archivo_salida, "w", newline="") as file:
        file.write(f"{archivo_entrada}\n")
        file.write(f"Ganancia maxima: {ganancia_maxima}\n")

        file.write("Plan de entrenamiento: ")
        n = len(plan_entrenamiento_optimo)
        for index, entrenamiento in enumerate(plan_entrenamiento_optimo):
            file.write(entrenamiento)
            if index != n - 1:
                file.write(", ")
