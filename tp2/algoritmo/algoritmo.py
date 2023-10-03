def _ganancias_parciales(n, esfuerzos, energias):
    matriz_ganancias = []
    for i in range(n):
        ganancias_dia = [0] * (i+1)
        for j in range(i+1):
            ganancias_dia[j] = _ganancia_parcial(i, j, esfuerzos[i], energias[j] , matriz_ganancias)
        matriz_ganancias.append(ganancias_dia)
    return matriz_ganancias

def _ganancia_parcial(i, j, esfuerzo_en_i, energia_en_j, matriz_ganancias):
    if i == 0:
        return _ganancia(esfuerzo_en_i, energia_en_j)

    if j == 0:
        return _ganancia(esfuerzo_en_i, energia_en_j) + _ganancia_maxima_dia_i(i - 2, matriz_ganancias)
   
    return _ganancia(esfuerzo_en_i, energia_en_j) + matriz_ganancias[i-1][j-1]

def _ganancia(esfuerzo_en_i, energia_en_j):
    return min(esfuerzo_en_i, energia_en_j)


def _ganancia_maxima(matriz_ganancias):
    return _ganancia_maxima_dia_i(len(matriz_ganancias) - 1, matriz_ganancias)

def _ganancia_maxima_dia_i(i, matriz_ganancias):
    if i == -1:
        return 0
    return max(matriz_ganancias[i])

def optimizar_entrenamiento(n, esfuerzos, energias):
    ganancias_parciales = _ganancias_parciales(n, esfuerzos, energias)
    ganancia_maxima = _ganancia_maxima(ganancias_parciales)
    plan_entrenamiento_optimo = _plan_entrenamiento_optimo_2(ganancias_parciales)
    return ganancia_maxima, plan_entrenamiento_optimo

def _plan_entrenamiento_optimo_2(matriz_ganancias):
    n = len(matriz_ganancias)
    return _plan_entrenamiento_optimo_rec_2(matriz_ganancias, n-1)

def _plan_entrenamiento_optimo_rec_2(matriz_ganancias, i):
    if i == -1:
        return []
    if i == 0:
        return ['Entreno']
    j_entrenamientos_consecutivos = _argmax(matriz_ganancias[i])
    if j_entrenamientos_consecutivos == i:
        return ((j_entrenamientos_consecutivos + 1) * ['Entreno'])
    return _plan_entrenamiento_optimo_rec_2(matriz_ganancias, i - j_entrenamientos_consecutivos - 2) + ['Descanso'] + ((j_entrenamientos_consecutivos + 1) * ['Entreno'])

def _plan_entrenamiento_optimo(matriz_ganancias):
    n = len(matriz_ganancias)
    resultados = [None] * n
    _plan_entrenamiento_optimo_rec(matriz_ganancias, resultados, n-1)
    return resultados

def _plan_entrenamiento_optimo_rec(matriz_ganancias, resultados, i):
    resultados[i] = "Entreno"
    if i == 0:
        return 
    
    j_entrenamientos_consecutivos = _argmax(matriz_ganancias[i])
    
    for k in range(1,j_entrenamientos_consecutivos + 1):
        resultados[i-k] = "Entreno"

    if i != j_entrenamientos_consecutivos:
        resultados[i-j_entrenamientos_consecutivos-1] = "Descanso"
    else:
        resultados[i-j_entrenamientos_consecutivos-1] = "Entreno"

    _plan_entrenamiento_optimo_rec(matriz_ganancias, resultados, i-2-j_entrenamientos_consecutivos)


def _argmax(lista):
    return lista.index(max(lista))