import random

random.seed(1)

class Compilado:
    def __init__(self, scaloni, ayudante):
        self.tiempo_scaloni = scaloni
        self.tiempo_ayudante = ayudante

    def __str__(self):
        return(self.tiempo_scaloni+ self.tiempo_ayudante)

def compilados_ordenados_de_forma_optima(compilados):
    return sorted(compilados, key=lambda compilado: compilado.tiempo_ayudante, reverse=True)

def tiempo_total(compilados_ordenados):
    tiempo_terminacion = []
    acumulador_tiempo_scaloni = 0
    for compilado in compilados_ordenados:
        acumulador_tiempo_scaloni += compilado.tiempo_scaloni
        tiempo_terminacion.append(acumulador_tiempo_scaloni + compilado.tiempo_ayudante)

    return max(tiempo_terminacion)
