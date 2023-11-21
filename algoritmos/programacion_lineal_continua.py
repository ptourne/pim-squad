import pulp


def hitting_set_pl_continua(b_array):
    problem = pulp.LpProblem("Scaloni", pulp.LpMinimize)
    dic_jugadores = {}

    # obtenemos b = "la cantidad de jugadores que pide el periodista más mufa"
    b = 0
    for periodista in b_array:
        if len(periodista) > b:
            b = len(periodista)

    for periodista in range(len(b_array)):
        dic_p = set()
        for jugador in b_array[periodista]:
            y = None
            if jugador in dic_jugadores:
                y = dic_jugadores[jugador]
            else:
                y = pulp.LpVariable(
                    f"y_{jugador}", lowBound=0, upBound=1, cat=pulp.LpContinuous)
                dic_jugadores[jugador] = y
            dic_p.add(y)

        p = pulp.lpSum(dic_p)
        problem += p >= 1
        problem += p <= len(dic_p)

    z = pulp.lpSum(dic_jugadores.values())
    problem += z

    problem.solve()
    res = pulp.value(z)

    jugadores_seleccionados = [
        jugador for jugador, variable in dic_jugadores.items() if pulp.value(variable) > 1/b]

    return res, jugadores_seleccionados
