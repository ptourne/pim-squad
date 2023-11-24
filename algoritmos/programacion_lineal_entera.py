import pulp


def hitting_set_pl_entera(b_array):
    problem = pulp.LpProblem("Scaloni", pulp.LpMinimize)
    dic_jugadores = {}

    for periodista in range(len(b_array)):
        set_p = set()
        for jugador in b_array[periodista]:
            y = None
            if jugador in dic_jugadores:
                y = dic_jugadores[jugador]
            else:
                y = pulp.LpVariable(f"y_{jugador}", cat=pulp.LpBinary)
                dic_jugadores[jugador] = y
            set_p.add(y)

        p = pulp.lpSum(set_p)
        problem += p >= 1
        problem += p <= len(set_p)

    z = pulp.lpSum(dic_jugadores.values())
    problem += z

    pulp.LpSolverDefault.msg = 0
    problem.solve()

    # Obtener jugadores seleccionados
    jugadores_seleccionados = [
        jugador for jugador, valor in dic_jugadores.items() if pulp.value(valor) > 0]

    return jugadores_seleccionados
