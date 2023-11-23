import os


def borrar_archivos():
    """
    Borra los archivos "datos.txt" y "resultados.txt" si existen.

    Returns:
        None
    """
    try:
        archivos_a_borrar = ["datos.txt", "resultados.txt"]
        for archivo in archivos_a_borrar:
            if os.path.exists(archivo):
                os.remove(archivo)
                # print(f"El archivo '{archivo}' ha sido eliminado.")
            else:
                # print(f"El archivo '{archivo}' no existe y no se pudo eliminar.")
                pass
    except Exception as e:
        print(f"Ocurrió un error al intentar borrar los archivos: {str(e)}")


# Ejemplo de uso
if __name__ == "__main__":
    borrar_archivos()
