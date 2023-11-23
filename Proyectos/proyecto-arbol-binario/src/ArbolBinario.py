class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, elemento):
        self.raiz = self._insertar_recursivo(self.raiz, elemento)
    def _insertar_recursivo(self, nodo, elemento):
        if nodo is None:
            return Nodo(elemento)
        elif elemento < nodo.valor:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, elemento)
        else:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, elemento)
        return nodo
       

    def eliminar(self, elemento):
        self.raiz = self._eliminar_recursivo(self.raiz, elemento)
    def _eliminar_recursivo(self, nodo, elemento):
        if nodo is None:
            return None
        
        elif elemento > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, elemento)
        elif elemento < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, elemento)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            minimo = self._minimo_recursivo(nodo.derecha)
            nodo.valor = minimo 
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, minimo)
        return nodo

    def existe(self, elemento):
        return self._existe_recursivo(self.raiz, elemento)
    
    def _existe_recursivo(self, nodo, elemento):
        if nodo is None:
            return False
        elif elemento == nodo.valor:
            return True
        elif elemento < nodo.valor:
            return self._existe_recursivo(nodo.izquierda, elemento)
        else:
            return self._existe_recursivo(nodo.derecha, elemento)
    def maximo(self):
        return self._maximo_recursivo(self.raiz)
    def _maximo_recursivo(self, nodo):
     if nodo is None:
        return None
     elif nodo.derecha is None:
        return nodo.valor
     else:
        return max(nodo.valor, self._maximo_recursivo(nodo.derecha))

    def minimo(self):
        return self._minimo_recursivo(self.raiz)
    
    def _minimo_recursivo(self, nodo):
     if nodo is None:
        return None
     elif nodo.izquierda is None:
        return nodo.valor
     else:
        return min(nodo.valor, self._minimo_recursivo(nodo.izquierda))

    def altura(self):
        return self._altura_recursiva(self.raiz)
    
    def _altura_recursiva(self, nodo):
        if nodo is None:
            return 0
        else:
            return 1 + max(self._altura_recursiva(nodo.izquierda), self._altura_recursiva(nodo.derecha))
    
    def obtener_elementos(self):
      elementos = []
      self._obtener_elementos_recursivo(self.raiz, elementos)
      return elementos
  
    def _obtener_elementos_recursivo(self, nodo, elementos):
        if nodo is None:
            return
        self._obtener_elementos_recursivo(nodo.izquierda, elementos)
        elementos.append(nodo.valor)
        self._obtener_elementos_recursivo(nodo.derecha, elementos)
          
    def __str__(self):
        lista = self._str_recursivo(self.raiz, []) 
        cadena = "[ " + " ".join(map(str, lista)) + " ]"
        return cadena

    def _str_recursivo(self, nodo, lista):
        if nodo is not None:
            lista = self._str_recursivo(nodo.izquierda, lista)
            lista.append(nodo.valor)
            lista = self._str_recursivo(nodo.derecha, lista)
        return lista