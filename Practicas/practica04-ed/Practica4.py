# Práctica 4
import unittest

#parte basada en el que realicé en la práctica 2 de tarea:
#hacer un juego de piedra papel o tijeras

def PPoT(piedrapapeltijeras):
    if piedrapapeltijeras == "piedra":
        return "papel"
    elif piedrapapeltijeras == "papel":
        return "tijeras"
    elif piedrapapeltijeras == "tijeras":
        return "piedra"
    else:
        return "no es un movimiento valido °՞(ᗒᗣᗕ)՞°"

#pruebas 

class PruebaPPoT(unittest.TestCase):

    def test_piedra_papel(self):
        resultado = PPoT("piedra")
        self.assertEqual(resultado, "papel") #true

    def test_papel_tijeras(self):
        resultado = PPoT("papel")
        self.assertEqual(resultado, "tijeras") #true

    def test_tijeras_piedra(self):
        resultado = PPoT("tijeras")
        self.assertEqual(resultado, "piedra") #true
        
    def test_entrada_invalida(self):
        resultado = PPoT("palabra")
        self.assertEqual(resultado, "Este input no es válido") #error
      
if __name__ == '__main__':
    unittest.main()
