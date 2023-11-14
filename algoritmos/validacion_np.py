def validar_solucion(C, B):
    """
    Valida si la solución es factible o no.
    :param C: solución
    :param B: conjuntos de jugadores pedidos por cada prensa
    :return: True si es factible, False en caso contrario
    """
    for i in range(len(B)):
        for j in range(len(C)):
            if C[j] in B[i]:
                break
            if j == len(C) - 1:
                return False
    return True
