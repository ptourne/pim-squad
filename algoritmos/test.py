from backtracking import bracktracking_hitting_set_problem
from programacion_lineal_entera import hitting_set_pl_entera
from validacion_np import validar_solucion
from manejo_archivos import obtener_subconjuntos
import unittest


class TestCatedra(unittest.TestCase):
    ########## BACKTRACKING ##########
    def test_5_txt_backtracking(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/5.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assert_(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 2)

    def test_7_txt_backtracking(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/7.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 2)

    def test_10_pocos_txt_backtracking(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/10_pocos.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 3)

    def test_10_todos_txt_backtracking(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/10_todos.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 10)

    def test_10_varios_txt_backtracking(self):
        subconjuntos = obtener_subconjuntos(
            "../ejemplos/catedra/10_varios.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 6)

    def test_15_txt_backtracking(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/15.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 4)

    def test_20_txt_backtracking(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/20.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 5)

    def test_50_txt_backtracking(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/50.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 6)

    def test_75_txt_backtracking(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/75.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 8)

    def test_100_txt_backtracking(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/100.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 9)

    def test_200_txt_backtracking(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/200.txt")
        solucion = bracktracking_hitting_set_problem(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 9)

    ########## PROGRAMACION LINEAL ENTERA ##########
    def test_5_txt_pl(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/5.txt")
        solucion = hitting_set_pl_entera(subconjuntos)
        self.assert_(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 2)

    def test_7_txt_pl(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/7.txt")
        solucion = hitting_set_pl_entera(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 2)

    def test_10_pocos_txt_pl(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/10_pocos.txt")
        solucion = hitting_set_pl_entera(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 3)

    def test_10_todos_txt_pl(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/10_todos.txt")
        solucion = hitting_set_pl_entera(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 10)

    def test_10_varios_txt_pl(self):
        subconjuntos = obtener_subconjuntos(
            "../ejemplos/catedra/10_varios.txt")
        solucion = hitting_set_pl_entera(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 6)

    def test_15_txt_pl(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/15.txt")
        solucion = hitting_set_pl_entera(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 4)

    def test_20_txt_pl(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/20.txt")
        solucion = hitting_set_pl_entera(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 5)

    def test_50_txt_pl(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/50.txt")
        solucion = hitting_set_pl_entera(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 6)

    def test_75_txt_pl(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/75.txt")
        solucion = hitting_set_pl_entera(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 8)

    def test_100_txt_pl(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/100.txt")
        solucion = hitting_set_pl_entera(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 9)

    def test_200_txt_pl(self):
        subconjuntos = obtener_subconjuntos("../ejemplos/catedra/200.txt")
        solucion = hitting_set_pl_entera(subconjuntos)
        self.assertTrue(validar_solucion(subconjuntos, solucion))
        self.assertEqual(len(solucion), 9)


# class NuestrosTests(unittest.TestCase):
#     ########## BACKTRACKING ##########
#     def test_5_txt_backtracking(self):
#         subconjuntos = obtener_subconjuntos("../ejemplos/nuestros/5.txt")
#         solucion = bracktracking_hitting_set_problem(subconjuntos)
#         self.assert_(validar_solucion(subconjuntos, solucion))
#         self.assertEqual(len(solucion), 2)

#     def test_7_txt_backtracking(self):
#         subconjuntos = obtener_subconjuntos("../ejemplos/nuestros/7.txt")
#         solucion = bracktracking_hitting_set_problem(subconjuntos)
#         self.assertTrue(validar_solucion(subconjuntos, solucion))
#         self.assertEqual(len(solucion), 2)

#     def test_10_pocos_txt_backtracking(self):
#         subconjuntos = obtener_subconjuntos("../ejemplos/nuestros/10_pocos.txt")
#         solucion = bracktracking_hitting_set_problem(subconjuntos)
#         self.assertTrue(validar_solucion(subconjuntos, solucion))
#         self.assertEqual(len(solucion), 3)

#     def test_10_todos_txt_backtracking(self):
#         subconjuntos = obtener_subconjuntos("../ejemplos/nuestros/10_todos.txt")
#         solucion = bracktracking_hitting_set_problem(subconjuntos)
#         self.assertTrue(validar_solucion(subconjuntos, solucion))
#         self.assertEqual(len(solucion), 10)

#     def test_10_varios_txt_backtracking(self):
#         subconjuntos = obtener_subconjuntos(
#             "../ejemplos/nuestros/10_varios.txt")
#         solucion = bracktracking_hitting_set_problem(subconjuntos)
#         self.assertTrue(validar_solucion(subconjuntos, solucion))
#         self.assertEqual(len(solucion), 6)

#     def test_15_txt_backtracking(self):
#         subconjuntos = obtener_subconjuntos("../ejemplos/nuestros/15.txt")
#         solucion = bracktracking_hitting_set_problem(subconjuntos)
#         self.assertTrue(validar_solucion(subconjuntos, solucion))
#         self.assertEqual(len(solucion), 4)

#     def test_20_txt_backtracking(self):
#         subconjuntos = obtener_subconjuntos("../ejemplos/nuestros/20.txt")
#         solucion = bracktracking_hitting_set_problem(subconjuntos)
#         self.assertTrue(validar_solucion(subconjuntos, solucion))

if __name__ == "__main__":
    unittest.main()
