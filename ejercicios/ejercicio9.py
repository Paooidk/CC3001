# -*- coding: utf-8 -*-
"""Ejercicio9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sCq8nEgrTwGCnLWKRVveHKlg8EJYq0kB

### Ejercicio 6.1 (Chequear si un árbol es AVL en tiempo lineal)

#Nombre: Paola López Neira

En este ejercicio usted debe modificar la implementación dada para asegurar que cada nodo del árbol se visite solo una vez, asegurando de esta manera que el costo de determinar si un árbol es AVL sea $\Theta(n)$.

Para esto, usted debe fusionar las funciones ``altura`` y ``es_AVL``en una sola función ``altura_AVL``, que retorne una tupla $(h,a)$, donde $h$ es la altura y $a$ es un booleano que dice si el árbol es AVL. De esta manera, al invocar la función se tiene de una sola vez toda la información necesaria.
"""

class Nodoi:
    def __init__(self, izq, info, der):
        self.izq=izq
        self.info=info
        self.der=der

    def altura(self):
        return 1+max(self.izq.altura(),self.der.altura())

    def es_AVL(self):
        return abs(self.izq.altura()-self.der.altura())<=1 \
                and self.izq.es_AVL() and self.der.es_AVL()

    def altura_AVL(self):
        a=self.izq.altura_AVL() #llamamos una vez a la tupla
        b=self.der.altura_AVL() #llamamos una vez a la tupla
        #¿por qué es lineal?
        #es lineal porque solo llamamos una vez al hijo obteniendo así un tiempo O(n)
        h = 1 + max(a[0], b[0]) #dado que es una tupla usamos [0] para obtener h
        a = abs(a[0]-b[0])<=1 and a[1] and b[1] #ahora usamos [1] para obtener a
        return (h,a) #se retorna (altura,es_AVL)


    def __str__(self):
        return "("+self.izq.__str__()+str(self.info)+self.der.__str__()+")"

class Nodoe:
    def __init__(self):
        pass

    def altura(self):
        return 0

    def es_AVL(self):
        return True

    def altura_AVL(self):
        return (0,True)

    def __str__(self):
        return"☐"

class Arbol:
    def __init__(self,raiz=Nodoe()):
        self.raiz=raiz

    def es_AVL(self):
        return self.raiz.es_AVL()

    def altura_AVL(self):
        return self.raiz.altura_AVL()

    def __str__(self):
        return self.raiz.__str__()

"""A continuación, pruébela con los dos árboles utilizados anteriormente:"""

a1=Arbol(Nodoi(Nodoi(Nodoe(),1,Nodoe()),
            2,
            Nodoi(Nodoe(),3,Nodoi(Nodoe(),4,Nodoe()))))
print(a1)
print(a1.es_AVL())
print(a1.altura_AVL())

a2=Arbol(Nodoi(Nodoi(Nodoe(),1,Nodoe()),
            2,
            Nodoi(Nodoe(),3,Nodoi(Nodoe(),4,Nodoi(Nodoe(),5,Nodoe())))))
print(a2)
print(a2.es_AVL())
print(a2.altura_AVL())