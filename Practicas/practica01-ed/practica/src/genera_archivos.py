import random


def enteros_aleatorios(num, file):
    """
    Genera y escribe 'num' enteros aleatorios en un archivo especificado.

    Args:
        num (int): Número de enteros aleatorios a generar.
        file (str): Nombre del archivo en el que se escribirán los enteros aleatorios.

    Returns:
        None
    """
    try:
        with open(file, "w") as archivo:
            for _ in range(num):
                numero = random.randint(
                    1, 100
                )  # Genera un número aleatorio entre 1 y 100
                archivo.write(str(numero) + "\n")
        print(f"Se han generado y escrito {num} enteros aleatorios en '{file}'.")
    except IOError as e:
        print(f"Ocurrió un error al escribir en el archivo '{file}': {str(e)}")


# Ejemplo de uso
if __name__ == "__main__":
    enteros_aleatorios(10, "numeros_aleatorios.txt")

import random


def enteros_aleatorios(num, file):
    """
    Genera y escribe 'num' enteros aleatorios en un archivo especificado.

    Args:
        num (int): Número de enteros aleatorios a generar.
        file (str): Nombre del archivo en el que se escribirán los enteros aleatorios.

    Returns:
        None
    """
    try:
        with open(file, "w") as archivo:
            for _ in range(num):
                numero = random.randint(
                    1, 100
                )  # Genera un número aleatorio entre 1 y 100
                archivo.write(str(numero) + "\n")
        print(f"Se han generado y escrito {num} enteros aleatorios en '{file}'.")
    except IOError as e:
        print(f"Ocurrió un error al escribir en el archivo '{file}': {str(e)}")

def operaciones_aritmeticas(operacion, valores, entero, file):
    """
    Realiza una operación aritmética especificada sobre una lista de valores y un entero, y escribe los resultados en un archivo especificado.

    Args:
        operacion (str): Operación aritmética a realizar. Puede ser "suma", "resta", "multiplicacion" o "division".
        valores (list): Lista de valores sobre los que se realizará la operación aritmética.
        entero (int): Entero sobre el que se realizará la operación aritmética.
        file (str): Nombre del archivo en el que se escribirán los resultados.

    Returns:
        None
    """
    try:
        with open(file, "w") as archivo:
            if operacion == "suma":
                for valor in valores:
                    archivo.write(str(valor + entero) + "\n")
            elif operacion == "resta":
                for valor in valores:
                    archivo.write(str(valor - entero) + "\n")
            elif operacion == "multiplicacion":
                for valor in valores:
                    archivo.write(str(valor * entero) + "\n")
            elif operacion == "division":
                for valor in valores:
                    archivo.write(str(valor / entero) + "\n")
    except IOError as e:
        print(f"Ocurrió un error al escribir en el archivo '{file}': {str(e)}")