def _ganancias_parciales(n, esfuerzos, energias):
    matriz_ganancias = []

    for i in range(n):
        ganancias_dia = [0] * (i + 1)
        for j in range(i + 1):
            ganancias_dia[j] = _ganancia_parcial(
                i, j, esfuerzos[i], energias[j], matriz_ganancias
            )
        matriz_ganancias.append(ganancias_dia)

    return matriz_ganancias


def _ganancia_parcial(i, j, esfuerzo_en_i, energia_en_j, matriz_ganancias):
    if i == 0:
        return _ganancia(esfuerzo_en_i, energia_en_j)

    if j == 0:
        return _ganancia(esfuerzo_en_i, energia_en_j) + _ganancia_maxima_dia_i(
            i - 2, matriz_ganancias
        )

    return _ganancia(esfuerzo_en_i, energia_en_j) + matriz_ganancias[i - 1][j - 1]


def _ganancia(esfuerzo_en_i, energia_en_j):
    return min(esfuerzo_en_i, energia_en_j)


def _ganancia_maxima(matriz_ganancias):
    return _ganancia_maxima_dia_i(len(matriz_ganancias) - 1, matriz_ganancias)


def _ganancia_maxima_dia_i(i, matriz_ganancias):
    if i == -1:
        return 0
    return max(matriz_ganancias[i])


def _plan_entrenamiento_optimo(matriz_ganancias):
    i = len(matriz_ganancias) - 1
    resultados = [None] * (i + 1)

    while i >= 0:
        j = matriz_ganancias[i].index(max(matriz_ganancias[i]))
        i = _obtener_resultados(i, j, resultados)

    return resultados


def _obtener_resultados(i, j, resultados):
    for _ in range(j, -1, -1):
        resultados[i] = "Entreno"
        i -= 1
    if i >= 0:
        resultados[i] = "Descanso"
        i -= 1
    return i


def optimizar_entrenamiento(n, esfuerzos, energias):
    ganancias_parciales = _ganancias_parciales(n, esfuerzos, energias)
    ganancia_maxima = _ganancia_maxima(ganancias_parciales)
    plan_entrenamiento_optimo = _plan_entrenamiento_optimo(ganancias_parciales)
    return ganancia_maxima, plan_entrenamiento_optimo

