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
    "Ricardo Centurión"
]


def generar_ejemplos(cant_prensas, cant_jug_max_por_prensa, devolver, direccion_archivo=""):
    prensas = []

    for _ in range(cant_prensas):
        cant_jugadores = random.randint(1, cant_jug_max_por_prensa)
        jugadores_elegidos = random.sample(JUGADORES, cant_jugadores)
        prensas.append(jugadores_elegidos)

    if devolver:
        return prensas

    with open(direccion_archivo, "w") as archivo:
        for prensa in prensas:
            for jugador in prensa[:len(prensa) - 1]:
                archivo.write(jugador + ",")
            archivo.write(prensa[len(prensa) - 1])
            archivo.write("\n")
    print(f"{direccion_archivo} generado con éxito")


# Posicionarse en la carpeta algoritmos y para correr el código
# cantidad de prensas, cantidad de jugadores por prensa, devolver=True o guardar en archivo=False, dirección del archivo de salida
# generar_ejemplos(100, 5, False, "../ejemplos/nuestros/100.txt")
