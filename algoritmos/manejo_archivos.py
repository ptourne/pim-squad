def obtener_subconjuntos(archivo):
    subconjuntos = []

    with open(archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            elementos = linea.split(',')
            set_elementos = set(elementos)
            subconjuntos.append(set_elementos)

    return subconjuntos
