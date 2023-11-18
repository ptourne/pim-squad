from backtracking import bracktracking_hitting_set_problem


def reduce_set_cover_to_hitting_set(dic_sets):
    b_array_dic = {}

    for p, i_set in dic_sets.items():
        for elemento in i_set:
            if elemento in b_array_dic:
                set_elemento = b_array_dic[elemento]
            else:
                set_elemento = set()
                b_array_dic[elemento] = set_elemento

            set_elemento.add(p)

    b_array = list(b_array_dic.values())

    return bracktracking_hitting_set_problem(b_array)


def prueba1():
    p1 = {'a', 'b', 'c'}
    p2 = {'c', 'a', 'd'}
    p3 = {'d', 'b', 'c'}
    p4 = {'b', 'd', 'a'}
    # p1,p4
    inicial = {'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4}

    res = reduce_set_cover_to_hitting_set(inicial)
    print(res)


def prueba2():
    p1 = {'a', 'c'}
    p2 = {'a'}
    p3 = {'d', 'b'}
    p4 = {'b', 'd', 'a'}
    # p1,p4
    inicial = {'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4}

    res = reduce_set_cover_to_hitting_set(inicial)
    print(res)


def prueba3():
    p1 = {'a', 'b', 'c'}
    p2 = {'b', 'd'}
    p3 = {'d', 'c'}
    p4 = {'d', 'e'}
    # p1,p4
    inicial = {'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4}

    res = reduce_set_cover_to_hitting_set(inicial)
    print(res)


def prueba4():
    p1 = {'a'}
    p2 = {'b'}
    p3 = {'c'}
    p4 = {'d'}
    p5 = {'e'}
    p6 = {'f'}
    p7 = {'g'}
    p8 = {'h'}
    p9 = {'i'}

    # p1,p4
    inicial = {'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4,
               'p5': p5, 'p6': p6, 'p7': p7, 'p8': p8, 'p9': p9}

    res = reduce_set_cover_to_hitting_set(inicial)
    print(res)


prueba4()
