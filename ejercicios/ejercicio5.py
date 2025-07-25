# -*- coding: utf-8 -*-
"""Ejercicio5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ne_S0hMZaKOQ9iCG1RJuYoZX2kc_fxJv

# Nombre: Paola López Neira

### Ejercicio 4.2
Escriba una función que pueda ser invocada como ``L.reversar()``, que al ejecutarse re-enlace los nodos de la lista de modo que queden en el orden opuesto al original, en tiempo lineal en el largo de la lista. Esto debe hacerse solo modificando punteros, sin crear nuevos nodos. Escriba a continuación la definición de la clase ``Lista`` incluyendo la función ``reversar``.
"""

!pip install aed_utilities

import aed_utilities as aed

class Nodo:
    def __init__(self, info, sgte=None):
        self.info=info
        self.sgte=sgte

class Lista:
    def __init__(self):
        self.primero=None

    def insertar_al_inicio(self,info):
        self.primero=Nodo(info,self.primero)

    def insertar_despues_de(self,p,info): # inserta después de nodo p
        p.sgte=Nodo(info,p.sgte)

    def eliminar_al_inicio(self):
        assert self.primero is not None
        self.primero=self.primero.sgte

    def eliminar_sgte_de(self,p): # elimina el nodo siguiente de p
        assert p.sgte is not None
        p.sgte=p.sgte.sgte

    def k_esimo(self,k): # retorna k-esimo nodo, o None si fuera de rango
        p=self.primero
        j=1
        while p is not None:
            if j==k:
                return p
            p=p.sgte
            j+=1
        return None

    def imprimir(self):
        p=self.primero
        while p is not None:
            print(p.info, end=" ")
            p=p.sgte
        print()

    def reversar(self):
        #Escribir código aquí
        A=None #Anterior
        S=None #Siguiente
        x=self.primero
        while x is not None:
          S=x.sgte
          x.sgte = A
          A=x
          x=S
        self.primero=A


    def dibujar(self):
      lld = aed.LinkedListDrawer(fieldHeader="primero", fieldData="info", fieldLink="sgte", strHeader="primero")
      lld.draw_linked_list(self)

"""Probar su función con los siguientes casos:"""

# Lista de varios elementos
L=Lista()
L.insertar_al_inicio(44)
L.insertar_al_inicio(13)
L.insertar_al_inicio(65)
L.insertar_al_inicio(42)
L.dibujar()
L.reversar()
L.dibujar()

# Lista vacía
L1 = Lista()
L1.dibujar()
L1.reversar()
L1.dibujar()

# Lista con un único elemento
L2 = Lista()
L2.insertar_al_inicio(12)
L2.dibujar()
L2.reversar()
L2.dibujar()