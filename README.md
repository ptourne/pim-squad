# TP2

## Como ejecutar el programa

El programa se corre desde el directorio `./tp2/algoritmos/` con un argumento que corresponde al archivo de entrada.

```bash
python main.py <ganancias_y_esfuerzos.txt>
```
Por defecto, el programa guardará el plan de entrenamiento óptimo en `./plan_entrenamiento_optimo.txt`, pero se puede especificar el destino esperado con `-o archivo_salida`.

Podemos correr el primer archivo de ejemplo con

```bash
python3 main.py ./algoritmos/input/nuestros_ejemplos/4.txt -o  ./algoritmos/output/nuestros_ejemplos/4.txt
```

## Tests

Podemos correr los tests del programa con

```bash
python3 test.py
```

Además se puede ver el seguimiento de los tests creados por nosotros con la herramienta excel la siguiente ruta a la planilla [./test./pruebas.xlsx](https://github.com/ptourne/pim-squad/blob/tp2/tp2/algoritmos/test/pruebas.xlsx)

## Medición de tiempo

Podemos generar el gráfico de tiempos que tarda el algoritmo con distintos tamaños de información con

```bash
python3 medicion_tiempo.py
```

# Informe

El informe se encuentra en [../informe/main.pdf](https://github.com/ptourne/pim-squad/blob/tp2/tp2/informe/main.pdf).
