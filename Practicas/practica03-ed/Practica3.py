# Práctica 3
#Autor:Epharedam
print("---------｡ﾟ•┈୨ ♡ ୧┈• ｡ﾟ----------") 
print("  Bienvenidx a Lista de tareas")
print("---------｡ﾟ•┈୨ ♡ ୧┈• ｡ﾟ----------") 

# lista de tareas pendientes
to_do_list = []

# Agregar una tarea pendiente a la lista
def agregar_tarea_pendiente():
    tarea = input("Ingrese la tarea que desea agregar: ")
    to_do_list.append(tarea)
    print("Tarea agregada. (๑'ᵕ'๑)⸝")
    print("---------｡ﾟ•┈୨ ♡ ୧┈• ｡ﾟ----------")
    
# Imprime la lista de tareas pendientes
def imprimir_lista_de_tareas_pendientes():
  print("Lista de tareas pendientes:")
  for i,tarea in enumerate(to_do_list, 1):
            print(f"{i}. {tarea}")
  print("---------｡ﾟ•┈୨ ♡ ୧┈• ｡ﾟ----------")

# marcar una tarea como completada
def marcar_como_realizada():
    numero_tarea = int(input("Ingrese el número de la tarea que desea marcar como completada: "))
    if 1 <= numero_tarea <= len(to_do_list):
        to_do_list[numero_tarea - 1] += "(✓)"
        print("Tarea marcada como completada.♡〜٩( ˃▿˂ )۶〜♡")
        print("˚. ✦.˳·˖✶ ⋆.✧̣̇˚.˚. ✦.˳·˖✶ ⋆.✧̣̇˚.")
    else:
         print("Número no válido.(⊙ _ ⊙ )")
         print("---------｡ﾟ•┈୨ ♡ ୧┈• ｡ﾟ----------")


# Elimina una tarea de la lista
def eliminar_tarea_pendiente():
    numero_tarea = int(input("Ingrese el número de la tarea que desea eliminar: "))
    if 1 <= numero_tarea <= len(to_do_list):
        tarea_eliminada = to_do_list.pop(numero_tarea - 1)
        print(f"Tarea '{tarea_eliminada}' fue borrada! ( ｡0ㅅ0｡)~✧")
    else:
         print("Número no válido°՞(ᗒᗣᗕ;)՞°")
         print("---------｡ﾟ•┈୨ ♡ ୧┈• ｡ﾟ----------")
    
def main():
  while True:
    print("1. Agregar tarea")
    print("2. Imprimir lista de tareas")
    print("3. Eliminar tarea ")
    print("4. Marcar tarea como realizada")
    print("5. Salir")
    print("---------｡ﾟ•┈୨ ♡ ୧┈• ｡ﾟ----------") 

    elección = input("Ingrese su elección: ")

    if elección == "1":
      agregar_tarea_pendiente()
    elif elección == "2":
      imprimir_lista_de_tareas_pendientes()
    elif elección == "3":
      eliminar_tarea_pendiente()
    elif elección == "4":
      marcar_como_realizada()
    elif elección == "5":
      print("Vuelve pronto ✧⁺⸜(●′▾‵●)⸝⁺✧")
      break
    else:
      print("No se reconoció tu solicitud .·°՞(≧o≦)՞°·. intenta de nuevo")
      print("    --------------｡ﾟ•┈୨ ♡ ୧┈• ｡ﾟ-----------------")

if __name__ == "__main__":
  main()