import random
import time

import numpy as np
from algoritmos import Video, videos_ordenados_de_forma_optima
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def tiempo_ejecucion(videos):
    tiempo_inicial = time.time()
    videos_ordenados_de_forma_optima(videos)
    tiempo_final = time.time()
    return tiempo_final - tiempo_inicial

def generar_videos_aleatorios(cant_videos):
    videos = []
    for _ in range(cant_videos):
        videos.append(Video(random.randint(1, 99999), random.randint(1, 99999)))
    return videos

def main():
    cantidad_elementos = []
    tiempos_ejecucion = []

    anterior = 0
    
    for n in range(1,1000):
        cantidad = 10*n
        if cantidad != anterior:
            videos_ejemplo = generar_videos_aleatorios(cantidad)
            cantidad_elementos.append(cantidad)
            tiempos_ejecucion.append(tiempo_ejecucion(videos_ejemplo) * 1000)
        anterior = cantidad 


    x = np.array(cantidad_elementos)
    y = np.array(tiempos_ejecucion)

    # Regresión Lineal
    coefficients = np.polyfit(x, y, 1)
    slope, intercept = coefficients
    linear_regression_line = slope * x + intercept

    # Regresión Logarítmica
    def n_logn_function(x, a):
        return a * x * np.log(x)
    params, covariance = curve_fit(n_logn_function, x, y)
    a = params[0]
    logaritmic_regression_line = a * x * np.log(x)

    # Graficar
    plt.scatter(x, y, label='Tiempo de ejecución', marker='o', color='blue')
    plt.plot(x, linear_regression_line, label='Regresión Linear', linestyle='-', color='red')
    plt.plot(x, logaritmic_regression_line, label='Regresión n log n', linestyle='-', color='green')

    # Add labels and a legend
    plt.xlabel('Cantidad de elementos')
    plt.ylabel('Tiempo de ejecución (ms)')
    plt.legend()
    plt.savefig('tiempos_ejecucion.png')
    plt.show()


main()