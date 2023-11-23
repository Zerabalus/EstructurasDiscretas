import sys
from src.genera_archivos import enteros_aleatorios
from src.borrador import borrar_archivos


def obtener_datos():
    return ("suma", 10)


def main():
    operacion, entero = obtener_datos()
    
    # Obtenemos los valores para operar con ellos
    archivo = "datos.txt"
    valores = []
    with open(archivo, "r") as f:
        for linea in f:
            valores.append(int(linea))
    
    # Operamos con los numeros y los guardamos en el archivo resultados
    with open("resultados.txt", "w") as f:
        if operacion == "suma":
            for valor in valores:
                f.write(str(valor + entero) + "\n")
        elif operacion == "resta":
            for valor in valores:
                f.write(str(valor - entero) + "\n")
        elif operacion == "multiplicacion":
            for valor in valores:
                f.write(str(valor * entero) + "\n")
        elif operacion == "division":
            for valor in valores:
                f.write(str(valor / entero) + "\n")


if __name__ == "__main__":
    borrar_archivos()
    num = 10
    archivo = "datos.txt"
    enteros_aleatorios(num, archivo)
    main()
