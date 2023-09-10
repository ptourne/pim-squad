import random, heapq, csv

random.seed(1)

class Video:
    def __init__(self, scaloni, ayudante):
        self.tiempo_scaloni = scaloni
        self.tiempo_ayudante = ayudante

def videos_ordenados_de_forma_optima(videos):
    return sorted(videos, key=lambda video: video.tiempo_scaloni, reverse=True)

def videos_en_archivo(nombre_archivo):
    videos = []

    with open(nombre_archivo, newline='') as archivo_tiempos:
        lector_csv = csv.reader(archivo_tiempos)
        videos.append(Video(lector_csv[0],lector_csv[1]))

    return videos


## 
def tiempo_total(videos_ordenados):
    """Devuelve el tiempo total de ejecución de los videos en la lista videos_ordenados."""
    tiempo_terminacion = []
    acumulador_tiempo_scaloni = 0
    for video in videos_ordenados:
        acumulador_tiempo_scaloni += video.tiempo_scaloni
        tiempo_terminacion.append(acumulador_tiempo_scaloni + video.tiempo_ayudante)

    return max(tiempo_terminacion)

def tiempo_optimo(videos):
    return tiempo_total(videos_ordenados_de_forma_optima(videos))

