# Práctica 4
#Autor:Epharedam
import unittest

#usaré un código basado en el que hicimos la práctica 2

class PPoT(unittest.TestCase):
# Prueba 1: Verifica si "piedra" devuelve "papel"
 def test_piedra_gana_papel():
    resultado = PPoT("piedra")
    assert resultado == "papel"

# Prueba 2: Verifica si "papel" devuelve "tijeras"
 def test_papel_gana_tijeras():
    resultado = PPoT("papel")
    assert resultado == "tijeras"

# Prueba 3: Verifica si "tijeras" devuelve "piedra"
 def test_tijeras_gana_piedra():
    resultado = PPoT("tijeras")
    assert resultado == "piedra"

 if __name__ == '__main__':
    test_piedra_gana_papel()
    test_papel_gana_tijeras()
    test_tijeras_gana_piedra()
