import random

JUGADORES = [
    "Emiliano Martínez",
    "Juan Musso",
    "Franco Armani",
    "Nicolás Tagliafico",
    "Marcos Acuña",
    "Cristian Romero",
    "Nicolás Otamendi",
    "Lucas Martínez Quarta",
    "Facundo Medina",
    "Germán Pezzella",
    "Nahuel Molina",
    "Gonzalo Montiel",
    "Juan Foyth",
    "Alexis Mac Allister",
    "Leandro Paredes",
    "Guido Rodríguez",
    "Exequiel Palacios",
    "Rodrigo de Paul",
    "Enzo Fernández",
    "Giovani Lo Celso",
    "Nicolas González",
    "Lucas Ocampos",
    "Alejandro Garnacho",
    "Julian Alvarez",
    "Lautaro Martínez",
    "Lucas Beltrán",
    "Lionel Messi",
    "Paulo Dybala",
    "Sergio Agüero",
    "Ángel Di María",
    "Joaquín Correa",
    "Nicolás Domínguez",
    "Matías Vargas",
    "Thiago Almada",
    "Mauro Icardi",
    "Cristian Pavón",
    "Agustín Urzi",
    "Brian Mansilla",
    "Ezequiel Barco",
    "Matías Zaracho",
    "Giovanni Simeone",
    "Maximiliano Romero",
    "Ricardo Centurión",
]


def generar_ejemplos_jugadores(
    cant_prensas: int,
    cant_jug_max_por_prensa: int,
    cant_max_opt: int,
    direccion_archivo="ejemplo_gen.txt",
):
    prensas = []
    divis_para_opt = cant_prensas // cant_max_opt
    jug_selecc = set()

    for i in range(cant_max_opt):
        jug_selecc_azar = random.choice(JUGADORES)
        while jug_selecc_azar in jug_selecc:
            jug_selecc_azar = random.choice(JUGADORES)
        print("Jugador seleccionado al azar: ", jug_selecc_azar)

        for _ in range(divis_para_opt):
            prensas.append([jug_selecc_azar])

        if i == cant_max_opt - 1:
            while len(prensas) < cant_prensas:
                prensas.append([jug_selecc_azar])

    for i in range(cant_prensas):
        cant_jugadores = random.randint(0, cant_jug_max_por_prensa)
        jugadores_elegidos = random.sample(JUGADORES, cant_jugadores - 1)
        prensas[i].extend(jugadores_elegidos)

        # Desordenamos los jugadores de esta prensa
        random.shuffle(prensas[i])

    random.shuffle(prensas)

    with open(direccion_archivo, "w") as archivo:
        for prensa in prensas:
            for jugador in prensa[: len(prensa) - 1]:
                archivo.write(jugador + ",")
            archivo.write(prensa[len(prensa) - 1])
            archivo.write("\n")
    print(f"{direccion_archivo} generado con éxito")


###### Para las pruebas de mediciones, requerimos generar ejemplos de mayor variabilidad, por ello implementamos lo siguiente ######


# hacemos una lista con las letras del abecedario
abecedario = []
for i in range(97, 123):
    abecedario.append(chr(i))


def generar_ejemplos_abc(
    cant_conjuntos: int,
    cant_letras: int,
    cant_min_subconjuntos: int,
    cant_max_subconjuntos: int,
    devolver: bool,
    cant_max_opt: int,
    direccion_archivo="ejemplo_gen_abc.txt",
):
    conjuntos = []
    divis_para_opt = cant_conjuntos // cant_max_opt
    comb_letras_selec = set()

    for i in range(cant_max_opt):
        letras = [str] * cant_letras
        for j in range(cant_letras):
            letras[j] = random.choice(abecedario)
        while "".join(letras) in comb_letras_selec:
            for j in range(cant_letras):
                letras[j] = random.choice(abecedario)
        letras = "".join(letras)
        for _ in range(divis_para_opt):
            letras_set = set()
            letras_set.add(letras)
            conjuntos.append(letras_set)
        if i == cant_max_opt - 1:
            while len(conjuntos) < cant_conjuntos:
                conjuntos.append(letras_set)

    for i in range(cant_conjuntos):
        cant_por_iter = random.randint(
            cant_max_subconjuntos, cant_max_subconjuntos)
        for _ in range(cant_por_iter):
            letras = [str] * cant_letras
            for j in range(cant_letras):
                letras[j] = random.choice(abecedario)
            letras = "".join(letras)
            letras_set = set()
            letras_set.add(letras)
            if i >= len(conjuntos):
                conjuntos.append(letras_set)
                conjuntos[i] = set(conjuntos[i])
            else:
                conjuntos[i].update(letras_set)

    if devolver:
        return conjuntos

    with open(direccion_archivo, "w") as archivo:
        for conjunto in conjuntos:
            i = 0
            for palabra in conjunto:
                if i < len(conjunto) - 1:
                    archivo.write(palabra + ",")
                else:
                    archivo.write(palabra)
                    archivo.write("\n")
                i += 1
    print(f"{direccion_archivo} generado con éxito")


# generar_ejemplos_abc(15, 5, 5, 2, False, 15,
#                      "../ejemplos/nuestros/abc/15.txt")
