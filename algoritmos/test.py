from backtracking import bracktracking_hitting_set_problem, es_compatible
from manejo_archivos import obtener_subconjuntos
import unittest


class TestCatedra(unittest.TestCase):
    def test_5_txt(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/5.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assert_(es_compatible(subconjuntos, solucion))
        self.assertEqual(len(solucion), 2)

    def test_7_txt(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/7.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(es_compatible(subconjuntos, solucion))
        self.assertEqual(len(solucion), 2)

    def test_10_pocos_txt(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/10_pocos.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(es_compatible(subconjuntos, solucion))
        self.assertEqual(len(solucion), 3)

    def test_10_todos_txt(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/10_todos.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(es_compatible(subconjuntos, solucion))
        self.assertEqual(len(solucion), 10)

    def test_10_varios_txt(self):
        subconjuntos = obtener_subconjuntos(
            "../ejemplos/catedra/10_varios.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(es_compatible(subconjuntos, solucion))
        self.assertEqual(len(solucion), 6)

    def test_15_txt(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/15.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(es_compatible(subconjuntos, solucion))
        self.assertEqual(len(solucion), 4)

    def test_20_txt(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/20.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(es_compatible(subconjuntos, solucion))
        self.assertEqual(len(solucion), 5)

    def test_50_txt(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/50.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(es_compatible(subconjuntos, solucion))
        self.assertEqual(len(solucion), 6)

    def test_75_txt(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/75.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(es_compatible(subconjuntos, solucion))
        self.assertEqual(len(solucion), 8)

    def test_100_txt(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/100.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(es_compatible(subconjuntos, solucion))
        self.assertEqual(len(solucion), 9)

    def test_200_txt(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/200.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(es_compatible(subconjuntos, solucion))
        self.assertEqual(len(solucion), 9)


# class TestNuestros(unittest.TestCase):
#     def test_5_muchos_txt(self):
#         subconjuntos = obtener_subconjuntos("../archivos_catedra/5_muchos.txt")
#         solucion = bracktracking_hitting_set_problem(subconjuntos)
#         self.assertTrue(es_compatible(subconjuntos, solucion))
#         self.assertEqual(len(solucion), 2)


if __name__ == "__main__":
    unittest.main()
