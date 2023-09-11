from manejo_archivos import compilados_en_archivo
from algoritmos import Compilado, compilados_ordenados_de_forma_optima, tiempo_total
import unittest


class TestPropios(unittest.TestCase):
    def test_tiempo_optimo_2_elementos_caso_1(self):
        compilados = [
            Compilado(scaloni=2, ayudante=3),
            Compilado(scaloni=3, ayudante=1)
        ]
        compilados_ordenados = compilados_ordenados_de_forma_optima(compilados)
        tiempo = tiempo_total(compilados_ordenados)
        self.assertEqual(tiempo, 6)

    
    def test_tiempo_optimo_2_elementos_caso_2(self):
        compilados = [
            Compilado(scaloni=2, ayudante=5),
            Compilado(scaloni=3, ayudante=1)
        ]
        compilados_ordenados = compilados_ordenados_de_forma_optima(compilados)
        tiempo = tiempo_total(compilados_ordenados)
        self.assertEqual(tiempo, 7)


    def test_tiempo_optimo_2_elementos_caso_3(self):
        compilados = [
            Compilado(scaloni=4, ayudante=3),
            Compilado(scaloni=2, ayudante=1)
        ]
        compilados_ordenados = compilados_ordenados_de_forma_optima(compilados)
        tiempo = tiempo_total(compilados_ordenados)
        self.assertEqual(tiempo, 7)

class TestEjemplosCatedra(unittest.TestCase):
    def test_tiempo_optimo_3_elementos(self):
        compilados = compilados_en_archivo("./datos-ejemplo/3-elem.txt")
        compilados_ordenados = compilados_ordenados_de_forma_optima(compilados)
        tiempo = tiempo_total(compilados_ordenados)
        self.assertEqual(tiempo, 10)

    def test_tiempo_optimo_10_elementos(self):
        compilados = compilados_en_archivo("./datos-ejemplo/10-elem.txt")
        compilados_ordenados = compilados_ordenados_de_forma_optima(compilados)
        tiempo = tiempo_total(compilados_ordenados)
        self.assertEqual(tiempo, 29)
        
    def test_tiempo_optimo_100_elementos(self):
        compilados = compilados_en_archivo("./datos-ejemplo/100-elem.txt")
        compilados_ordenados = compilados_ordenados_de_forma_optima(compilados)
        tiempo = tiempo_total(compilados_ordenados)
        self.assertEqual(tiempo, 5223)
        
    def test_tiempo_optimo_10000_elementos(self):
        compilados = compilados_en_archivo("./datos-ejemplo/10000-elem.txt")
        compilados_ordenados = compilados_ordenados_de_forma_optima(compilados)
        tiempo = tiempo_total(compilados_ordenados)
        self.assertEqual(tiempo, 497886735)


if __name__ == '__main__':
    unittest.main()
