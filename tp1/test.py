from algoritmos import videos_ordenados_de_forma_optima, videos_en_archivo, tiempo_total
import unittest


class TestEjemplos(unittest.TestCase):
    def test_tiempo_optimo_3_elementos(self):
        videos = videos_en_archivo("./datos-ejemplo/3-elem.txt")
        videos_ordenados = videos_ordenados_de_forma_optima(videos)
        tiempo = tiempo_total(videos_ordenados)
        self.assertEqual(tiempo, 10)

    def test_tiempo_optimo_10_elementos(self):
        videos = videos_en_archivo("./datos-ejemplo/10-elem.txt")
        videos_ordenados = videos_ordenados_de_forma_optima(videos)
        tiempo = tiempo_total(videos_ordenados)
        self.assertEqual(tiempo, 29)
        
    def test_tiempo_optimo_100_elementos(self):
        videos = videos_en_archivo("./datos-ejemplo/100-elem.txt")
        videos_ordenados = videos_ordenados_de_forma_optima(videos)
        tiempo = tiempo_total(videos_ordenados)
        self.assertEqual(tiempo, 5223)
        
    def test_tiempo_optimo_10000_elementos(self):
        videos = videos_en_archivo("./datos-ejemplo/10000-elem.txt")
        videos_ordenados = videos_ordenados_de_forma_optima(videos)
        tiempo = tiempo_total(videos_ordenados)
        self.assertEqual(tiempo, 497886735)


if __name__ == '__main__':
    unittest.main()
