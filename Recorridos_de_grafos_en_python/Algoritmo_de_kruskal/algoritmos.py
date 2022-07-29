import math
from queue import PriorityQueue
from pprint import pformat

def distancia_euclidiana(x_1, y_1, x_2, y_2):
   dx = (x_2 - x_1)**2
   dy = (y_2 - y_1)**2
   distancia = math.sqrt((dx + dy))
   return distancia

def prim(grafo, origen):
   visitados = list()
   recorrido = list()
   pq = PriorityQueue()
   visitados.append(origen)
   adyacentes = grafo[origen]
   for nodo in adyacentes:
      pq.put((nodo[1], origen, nodo[0]))

   while not pq.empty():
      arista = pq.get()
      destino = arista[2]
      if destino not in visitados:
         visitados.append(destino)
         adyacentes = grafo[destino]
         for nodo in adyacentes:
            pq.put((nodo[1], destino, nodo[0]))
         recorrido.append(arista)

   return recorrido

def union(lista, pos1, pos2):
   for valor in lista[pos2]:
      lista[pos1].append(valor)
   lista.pop(pos2)
   
def findSet(lista, value):
   i = 0
   while i <len(lista):
      for valor in lista[i]:
         if valor == value:
            return i
      i += 1
   return -1
   
def alg_kruskal(grafo):
   kruskal = dict()
   pq = PriorityQueue()
   disjuntos = []
   visitados = []
   for key in grafo:
      for value in grafo[key]:
         arista1 = (value[1], (key, value[0]))
         arista2 = (value[1], (value[0], key))
         if arista1 not in visitados and arista2 not in visitados:
            visitados.append(arista1)
            pq.put(arista1)
      disjuntos.append([key])

   print(disjuntos)
   while not pq.empty():
      arista = pq.get()
      p1 = findSet(disjuntos, arista[1][0])
      p2 = findSet(disjuntos, arista[1][1])
      if p1 != p2:
         kruskal[arista[1]] = arista[0]
         union(disjuntos, p1, p2)
      print("Arista: ", arista)
      print(disjuntos)
   return kruskal
        



