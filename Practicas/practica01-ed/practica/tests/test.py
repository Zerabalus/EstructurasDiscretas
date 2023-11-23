import unittest
import os
from io import StringIO
import sys

# Importa las funciones que deseas probar
from main import obtener_datos, main


class TestObtenerDatos(unittest.TestCase):
    def test_obtener_datos_argumentos_correctos(self):
        # Simula argumentos de línea de comandos válidos
        sys.argv = ["main.py", "suma", "5"]
        resultado = obtener_datos()
        self.assertEqual(resultado, ("suma", 5))

    def test_obtener_datos_argumentos_incorrectos(self):
        # Simula argumentos de línea de comandos incorrectos
        sys.argv = ["main.py", "suma"]
        with self.assertRaises(SystemExit):
            obtener_datos()

    def test_enteros_aleatorios_valor_invalido(self):
        sys.argv = ["main.py", "division", "0"]
        # Simula la llamada a la función con un valor inválido (0)
        # with self.assertRaises(MiExcepcionPersonalizada):
        with self.assertRaises(ValueError):
            obtener_datos()


class TestMain(unittest.TestCase):
    def test_multiplicacion(self):
        # Limpia el archivo resultados.txt antes de ejecutar la prueba
        if os.path.exists("resultados.txt"):
            os.remove("resultados.txt")

        # Simula una operación de multiplicación
        with open("datos.txt", "w") as archivo:
            archivo.write("2\n3\n4\n")

        # Simula argumentos de línea de comandos para la multiplicación
        sys.argv = ["main.py", "multiplicacion", "5"]

        # Redirige la salida estándar para capturarla
        sys.stdout = StringIO()

        # Ejecuta la función main
        main()

        # Restaura la salida estándar
        sys.stdout = sys.__stdout__

        # Verifica que el resultado de la multiplicación se haya escrito en el archivo resultados.txt
        with open("resultados.txt", "r") as archivo_resultados:
            resultado = archivo_resultados.read().strip()
        self.assertEqual(resultado, "10\n15\n20")

    def test_resta(self):
        # Limpia el archivo resultados.txt antes de ejecutar la prueba
        if os.path.exists("resultados.txt"):
            os.remove("resultados.txt")

        # Simula una operación de resta
        with open("datos.txt", "w") as archivo:
            archivo.write("10\n20\n30\n")

        # Simula argumentos de línea de comandos para la resta
        sys.argv = ["main.py", "resta", "5"]

        # Redirige la salida estándar para capturarla
        sys.stdout = StringIO()

        # Ejecuta la función main
        main()

        # Restaura la salida estándar
        sys.stdout = sys.__stdout__

        # Verifica que el resultado de la resta se haya escrito en el archivo resultados.txt
        with open("resultados.txt", "r") as archivo_resultados:
            resultado = archivo_resultados.read().strip()
        self.assertEqual(resultado, "5\n15\n25")

    def test_division(self):
        # Limpia el archivo resultados.txt antes de ejecutar la prueba
        if os.path.exists("resultados.txt"):
            os.remove("resultados.txt")

        # Simula una operación de división
        with open("datos.txt", "w") as archivo:
            archivo.write("20\n30\n40\n")

        # Simula argumentos de línea de comandos para la división
        sys.argv = ["main.py", "division", "5"]

        # Redirige la salida estándar para capturarla
        sys.stdout = StringIO()

        # Ejecuta la función main
        main()

        # Restaura la salida estándar
        sys.stdout = sys.__stdout__

        # Verifica que el resultado de la división se haya escrito en el archivo resultados.txt
        with open("resultados.txt", "r") as archivo_resultados:
            resultado = archivo_resultados.read().strip()
        self.assertEqual(resultado, "4.0\n6.0\n8.0")

    def test_suma(self):
        # Limpia el archivo resultados.txt antes de ejecutar la prueba
        if os.path.exists("resultados.txt"):
            os.remove("resultados.txt")

        # Simula una operación de resta
        with open("datos.txt", "w") as archivo:
            archivo.write("10\n20\n30\n")

        # Simula argumentos de línea de comandos para la resta
        sys.argv = ["main.py", "suma", "5"]

        # Redirige la salida estándar para capturarla
        sys.stdout = StringIO()

        # Ejecuta la función main
        main()

        # Restaura la salida estándar
        sys.stdout = sys.__stdout__

        # Verifica que el resultado de la resta se haya escrito en el archivo resultados.txt
        with open("resultados.txt", "r") as archivo_resultados:
            resultado = archivo_resultados.read().strip()
        self.assertEqual(resultado, "15\n25\n35")


# class TestOtrosProblemas(unittest.TestCase):
# def test_main_archivo_no_encontrado(self):
#     # Simula que el archivo 'datos.txt' no existe
#     if os.path.exists("datos.txt"):
#         os.remove("datos.txt")

#     # Redirige la salida estándar para capturarla
#     sys.stdout = StringIO()

#     # Ejecuta la función main
#     main()

#     # Restaura la salida estándar
#     sys.stdout = sys.__stdout__

#     # Verifica que se imprima el mensaje de error
#     self.assertEqual(sys.stdout.getvalue().strip(), "El archivo no se encontró.")

# def test_main_excepcion_lectura_archivo(self):
#     # Simula una excepción al leer el archivo 'datos.txt'
#     with open("datos.txt", "w") as archivo:
#         archivo.write("1\n2\n3\n")

#     # Cambia los permisos del archivo para simular un error de lectura
#     os.chmod("datos.txt", 0o222)

#     # Redirige la salida estándar para capturarla
#     sys.stdout = StringIO()

#     # Ejecuta la función main
#     main()

#     # Restaura la salida estándar
#     sys.stdout = sys.__stdout__

#     # Verifica que se imprima el mensaje de error
#     self.assertEqual(
#         sys.stdout.getvalue().strip(), "Ocurrió un error al leer el archivo."
#     )

# def test_main_excepcion_escritura_archivo(self):
#     # Simula una excepción al escribir en el archivo 'resultados.txt'
#     with open("datos.txt", "w") as archivo:
#         archivo.write("1\n2\n3\n")

#     # Cambia los permisos del archivo para simular un error de escritura
#     os.chmod("resultados.txt", 0o444)

#     # Redirige la salida estándar para capturarla
#     sys.stdout = StringIO()

#     # Ejecuta la función main
#     main()

#     # Restaura la salida estándar
#     sys.stdout = sys.__stdout__

#     # Verifica que se imprima el mensaje de error
#     self.assertIn(
#         "Ocurrió un error al escribir en el archivo:", sys.stdout.getvalue().strip()
#     )

if __name__ == "__main__":
    unittest.main()
