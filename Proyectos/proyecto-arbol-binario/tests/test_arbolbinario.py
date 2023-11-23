import pytest
from src.ArbolBinario import ArbolBinario

@pytest.fixture
def arbol():
    arbol = ArbolBinario()
    elementos = [5, 3, 7, 2, 4, 6, 8, 11]

    for elemento in elementos:
        arbol.insertar(elemento)

    return arbol

def test_insertar(arbol):
    arbol.insertar(9)
    assert arbol.existe(9)

def test_eliminar(arbol):
    assert arbol.existe(7)
    arbol.eliminar(7)
    assert not arbol.existe(7)

def test_existe(arbol):
    assert arbol.existe(4)

    elemento_inexistente = 10
    assert not arbol.existe(elemento_inexistente)

def test_maximo(arbol):
    assert arbol.maximo() == max(arbol.obtener_elementos())

def test_minimo(arbol):
    assert arbol.minimo() == min(arbol.obtener_elementos())

def test_altura(arbol):
    assert arbol.altura() == 4

def test_str(arbol):
    expected_str = "[ " + " ".join(map(str, sorted(arbol.obtener_elementos()))) + " ]"
    assert str(arbol) == expected_str

if __name__ == "__main__":
    pytest.main()
