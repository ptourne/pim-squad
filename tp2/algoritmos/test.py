import unittest
import subprocess


def correr(comando):
    try:
        result = subprocess.run(
            comando,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return result.stdout, result.stderr
    except Exception as e:
        return None, str(e)


def resultados(path_relativo):
    archivo_entrada = f"./test/input/{path_relativo}"
    path_salida = f"./test/output/{path_relativo}"
    path_salida_esperada = f"./test/output_esperado/{path_relativo}"

    correr(f"python3 main.py -o {path_salida} {archivo_entrada}")

    with open(path_salida_esperada, "r") as archivo:
        salida_esperada = archivo.read()

    with open(path_salida, "r") as archivo:
        salida = archivo.read()
    return salida_esperada, salida


class TestEjemplosCatedra(unittest.TestCase):
    def test_ej_catedra_3(self):
        salida_esperada, salida = resultados("ejemplos_catedra/3.txt")
        self.assertEqual(salida_esperada, salida)

    def test_ej_catedra_10(self):
        salida_esperada, salida = resultados("ejemplos_catedra/10.txt")
        self.assertEqual(salida_esperada, salida)
    
    def test_ej_catedra_10_bis(self):
        salida_esperada, salida = resultados("ejemplos_catedra/10_bis.txt")
        self.assertEqual(salida_esperada, salida)

    def test_ej_catedra_10_todo_entreno(self):
        salida_esperada, salida = resultados("ejemplos_catedra/10_todo_entreno.txt")
        self.assertEqual(salida_esperada, salida)

    def test_ej_catedra_50(self):
        salida_esperada, salida = resultados("ejemplos_catedra/50.txt")
        self.assertEqual(salida_esperada, salida)

    def test_ej_catedra_50_bis(self):
        salida_esperada, salida = resultados("ejemplos_catedra/50_bis.txt")
        self.assertEqual(salida_esperada, salida)

    def test_ej_catedra_100(self):
        salida_esperada, salida = resultados("ejemplos_catedra/100.txt")
        self.assertEqual(salida_esperada, salida)

    def test_ej_catedra_500(self):
        salida_esperada, salida = resultados("ejemplos_catedra/500.txt")
        self.assertEqual(salida_esperada, salida)

    def test_ej_catedra_1000(self):
        salida_esperada, salida = resultados("ejemplos_catedra/1000.txt")
        self.assertEqual(salida_esperada, salida)

    def test_ej_catedra_1000(self):
        salida_esperada, salida = resultados("ejemplos_catedra/1000.txt")
        self.assertEqual(salida_esperada, salida)

    
    def test_nuestros_ejemplos_4(self):
        salida_esperada, salida = resultados("nuestros_ejemplos/4.txt")
        self.assertEqual(salida_esperada, salida)

    def test_nuestros_ejemplos_energias_escalera_10(self):
        salida_esperada, salida = resultados("nuestros_ejemplos/energias_escalera_10.txt")
        self.assertEqual(salida_esperada, salida)
    
    def test_nuestros_ejemplos_energias_escalera_(self):
        salida_esperada, salida = resultados("nuestros_ejemplos/energias_escalera.txt")
        self.assertEqual(salida_esperada, salida)

    def test_nuestros_ejemplos_energias_iguales(self):
        salida_esperada, salida = resultados("nuestros_ejemplos/energias_iguales.txt")
        self.assertEqual(salida_esperada, salida)

    def test_nuestros_ejemplos_energias_iguales(self):
        salida_esperada, salida = resultados("nuestros_ejemplos/energias_iguales.txt")
        self.assertEqual(salida_esperada, salida)


if __name__ == "__main__":
    unittest.main()
