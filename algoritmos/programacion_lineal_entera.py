import pulp


def sol_por_prog_lineal(b_array):
    problem = pulp.LpProblem("Scaloni", pulp.LpMinimize)
    dic_jugadores = {}

    for periodista in range(len(b_array)):
        dic_p = set()
        for jugador in b_array[periodista]:
            y = None
            if jugador in dic_jugadores:
                y = dic_jugadores[jugador]
            else:
                y = pulp.LpVariable(f"y_{jugador}", cat=pulp.LpBinary)
                dic_jugadores[jugador] = y
            dic_p.add(y)

        p = pulp.lpSum(dic_p)
        # problem += p
        problem += p >= 1
        problem += p <= len(dic_p)

    z = pulp.lpSum(dic_jugadores.values())
    problem += z

    problem.solve()
    return int(pulp.value(z.value()))
