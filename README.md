# TP1

## Como ejecutar el programa

El programa se corre desde el directorio `/tp1/` con un argumento que corresponde al archivo de entrada.

```bash
python main.py <compilados_a_ordenar.csv>
```

Por defecto, el programa guardará el conjunto de compilados ordenados en `./compilados_ordenados.csv`, pero se puede especificar el destino esperado con `-o archivo_salida`.

Podemos correr el primer archivo de ejemplo con

```bash
python main.py -o ./ejemplo-3-elem-ordenados.csv ./datos-ejemplo/3-elem.txt
```

## Tests

Podemos correr los tests del programa con

```bash
python test.py
```

## Medición de tiempo

Podemos generar el gráfico de tiempos que tarda el algoritmo con distintos tamaños de información con

```bash
python test.py
```

# Informe

El informe se encuentra en `./tp1/informe-V2023-09-17.pdf`
