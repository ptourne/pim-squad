import random, heapq, csv

random.seed(1)

class Video:
    def __init__(self, scaloni, ayudante):
        self.tiempo_scaloni = scaloni
        self.tiempo_ayudante = ayudante

    def __format__(self):
        return (self.tiempo_scaloni, self.tiempo_ayudante)
    
    def __str__(self):
        return(self.tiempo_scaloni+ self.tiempo_ayudante)
    

def videos_ordenados_de_forma_optima(videos): # O(N * log(N)) por timsort
    return sorted(videos, key=lambda video: video.tiempo_ayudante, reverse=True)


def videos_en_archivo(nombre_archivo):
    videos = []

    with open(nombre_archivo, newline='') as archivo_tiempos:
        lector_csv = csv.reader(archivo_tiempos)
        next(lector_csv, None)
        for fila in lector_csv:
            videos.append(Video(int(fila[0]),int(fila[1])))
    return videos

def tiempo_total(videos_ordenados): # O(N)
    tiempo_terminacion = []
    acumulador_tiempo_scaloni = 0
    for video in videos_ordenados:
        acumulador_tiempo_scaloni += video.tiempo_scaloni
        tiempo_terminacion.append(acumulador_tiempo_scaloni + video.tiempo_ayudante)

    return max(tiempo_terminacion)

def tiempo_optimo(videos):
    return tiempo_total(videos_ordenados_de_forma_optima(videos))

