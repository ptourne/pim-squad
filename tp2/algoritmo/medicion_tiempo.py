import random
import time

import numpy as np
from sklearn.metrics import mean_squared_error
from algoritmo import optimizar_entrenamiento
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import gaussian_kde

def tiempo_ejecucion(n, esfuerzos, energias):
    tiempo_inicial = time.process_time()
    optimizar_entrenamiento(n, esfuerzos, energias)
    tiempo_final = time.process_time()
    return tiempo_final - tiempo_inicial

def generar_esfuerzos_y_energias_aleatorios(n, esfuerzo_maximo, energia_maxima):
    esfuerzos = [random.randint(1, esfuerzo_maximo) for _ in range(n)]
    energias = [random.randint(1, energia_maxima) for _ in range(n)]
    energias = sorted(energias, reverse=True)
    return esfuerzos, energias

def main():
    graficar_simulaciones(1000, 5, 100, 100, "./informe/img/tiempos_puntos.png", "./informe/img/tiempos_densidad.png", 10, 10, 7)

def graficar_simulaciones(maximo, intervalos, esfuerzo_maximo, energia_maxima, path_salida_puntos, path_salida_densidad, numero_vueltas, numero_muestras_por_cantidad, group_size):
    cantidad_compilados = list(range(1, maximo, intervalos))
    muestras_compilados = []
    mediciones = []

    # Se genera la matriz <muestras_compilados> de tamaño [numero_muestras_por_cantidad][len(cantidad_compilados)]
    # la cual contiene por cada cantidad_compilados, numero_muestras_por_cantidad diferentes escenarios. 
    # Además, se inicializa una matriz de mediciones de igual tamaño con ceros.
    for i in range(numero_muestras_por_cantidad):
        escenarios_muestras_compilados = []
        mediciones_aux = []
        for cantidad in cantidad_compilados:
            escenarios_muestras_compilados.append(generar_esfuerzos_y_energias_aleatorios(cantidad, esfuerzo_maximo, energia_maxima))
            mediciones_aux.append(0)
        muestras_compilados.append(escenarios_muestras_compilados)
        mediciones.append(mediciones_aux)

    # Se recorre la matriz de muestras y se mide el tiempo de ordenamiento para cada una, vueltas veces
    # sumando cada medición al casillero correspondiente en la matriz mediciones.
    for _ in range(numero_vueltas):
        for index_muestras_por_cantidad, muestras_por_cantidad in enumerate(muestras_compilados):
            for index_muestra, muestra in enumerate(muestras_por_cantidad):
                mediciones[index_muestras_por_cantidad][index_muestra] += tiempo_ejecucion(len(muestra[0]), muestra[0], muestra[1]) * 1000
    
    # Se recorre la matriz de mediciones dividiendo cada casillero por numero_vueltas para obtener
    # el promedio de las mediciones
    for index_muestras_por_cantidad, muestras_por_cantidad in enumerate(muestras_compilados):
        for index_muestra, muestra in enumerate(muestras_por_cantidad):
            mediciones[index_muestras_por_cantidad][index_muestra] /= numero_vueltas
    

    # Se aplana la matriz mediciones y se concatena cantidad_compilados numero_vueltas veces
    tiempos_ejecucion = [item for sublist in mediciones for item in sublist]
    cantidad_compilados *= numero_muestras_por_cantidad

    # Agrupamos al vector de mediciones y al vector de cantidad_compilados para esa medición
    # para poder ordernarlos de tal manera que la cantidad quede en forma creciente.
    # Luego los desagrupamos
    sorted_pairs = sorted(zip(cantidad_compilados, tiempos_ejecucion), key=lambda pair: pair[0])
    cantidad_compilados_ordenados, tiempos_ejecucion_ordenados = zip(*sorted_pairs)

    x = np.array(cantidad_compilados_ordenados)
    y = np.array(tiempos_ejecucion_ordenados)

    exportar_grafico_puntos(x, y, group_size, path_salida_puntos, numero_muestras_por_cantidad)
    exportar_grafico_densidad(x, y, path_salida_densidad)

def exportar_grafico_puntos(x, y, tamanio_grupos_cuantiles, path_salida, numero_muestras_por_cantidad):
    # Graficar
    plt.figure(dpi=600)

    X = np.array(x)
    Y = np.array(y)

    # Regresión cuadrática
    def a_x_function(x, a, b, c):
        return a * pow(x,2) + b * x + c

    params, _ = curve_fit(a_x_function, x, y)
    a = params[0]
    b = params[1]
    c = params[2]
    cuadratic_regression_curve = a * pow(x,2) + b * x + c

    # Calcular el RMSE (Root mean square error) para la regresión cuadrática
    rmse_cuadratica = np.sqrt(mean_squared_error(y, cuadratic_regression_curve))

 
    # Regresión exponencial
    def a_x_function(x, a, b):
        return pow(a, x) + b

    params, _ = curve_fit(a_x_function, x, y)
    a = params[0]
    b = params[1]
    exponential_regression_curve = pow(a, x) + b

    # Calcular el RMSE (Root mean square error) para la regresión exponencial
    rmse_exponencial = np.sqrt(mean_squared_error(y, exponential_regression_curve))

    # Determinar número de grupos
    num_groupos = (len(x) // numero_muestras_por_cantidad) - tamanio_grupos_cuantiles + 1
    
    # Inicializar arreglos para almacenar cuantiles
    cuantiles_25 = np.zeros(num_groupos)
    cuantiles_75 = np.zeros(num_groupos)

    centros_grupos = []

    # Calcular cuantiles para cada grupo y el centro de cada uno
    for i in range(num_groupos):
        j = i * numero_muestras_por_cantidad
        j_s = (i + tamanio_grupos_cuantiles) * numero_muestras_por_cantidad

        group_y = Y[j:j_s]
        cuantiles_25[i] = np.percentile(group_y, 25)
        cuantiles_75[i] = np.percentile(group_y, 75)
        centro_grupo = np.mean(X[j:j_s])
        centros_grupos.append(centro_grupo)

    centros_grupos = np.array(centros_grupos)
    # Plot the lines
    plt.plot(centros_grupos, cuantiles_75, label='Q0.75', color="darkgreen", linewidth=0.75)
    plt.plot(centros_grupos, cuantiles_25, label='Q0.25', color="firebrick", linewidth=0.75)

    plt.scatter(
        x, y, label="Tiempo de ejecución", marker="o", color="lightsteelblue", alpha=0.7, s=0.8
    )
    plt.plot(
        x,
        cuadratic_regression_curve,
        label="Regresión cuadrática",
        linestyle="-",
        color="darkmagenta",
        linewidth=1,
    )
    plt.plot(
        x,
        exponential_regression_curve,
        label="Regresión exponencial",
        linestyle="-",
        color="navy",
        linewidth=1,
    )

    # Anotamos el rmse de cada regresión
    plt.annotate(
        f"RMSE n^2: {rmse_cuadratica:.5f}",
        (0.02, 0.62),
        xycoords="axes fraction",
        fontsize=8,
        color="darkmagenta",
    )

    plt.annotate(
        f"RMSE a^n: {rmse_exponencial:.5f}",
        (0.02, 0.57),
        xycoords="axes fraction",
        fontsize=8,
        color="navy",
    )

    # Etiquetas y leyenda
    plt.xlabel("Cantidad de compilados")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.legend()
    plt.title("Tiempo de ejecución del algoritmo de ordenamiento")
    plt.savefig(path_salida)


def exportar_grafico_densidad(x, y, path_salida):
    # Graficar
    plt.figure(dpi=600)

    X = np.array(x)
    Y = np.array(y)

    # Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents
    nbins=1200
    k = gaussian_kde([x,y])
    xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))
    
    # Make the plot
    c = plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='auto', cmap='Blues')
    plt.colorbar(c, format='')

    # Etiquetas y leyenda
    plt.xlabel("Cantidad de compilados")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.legend()
    plt.title("Densidad de mediciones de tiempo de ejecución del algoritmo de ordenamiento")
    plt.savefig(path_salida)


main()
