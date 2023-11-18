import random


def generador_de_ejemplos(cant_prensas, cant_jug_max_por_prensa, direccion_archivo):
    jugadores = [
        "Emiliano Martínez",
        "Walter Benítez",
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
        "Adolfo Gaich",
        "Mauro Icardi",
        "Cristian Pavón",
        "Agustín Urzi",
        "Brian Mansilla",
        "Ezequiel Barco",
        "Matías Zaracho",
        "Giovanni Simeone",
        "Maximiliano Romero",
        "Ricardo Centurión"
    ]

    prensas = []

    for _ in range(cant_prensas):
        cant_jugadores = random.randint(1, cant_jug_max_por_prensa)
        jugadores_elegidos = random.sample(jugadores, cant_jugadores)
        prensas.append(jugadores_elegidos)

    with open(direccion_archivo, "w") as archivo:
        for prensa in prensas:
            for jugador in prensa[:len(prensa) - 1]:
                archivo.write(jugador + ",")
            archivo.write(prensa[len(prensa) - 1])
            archivo.write("\n")


generador_de_ejemplos(10, 10, "10.txt")
