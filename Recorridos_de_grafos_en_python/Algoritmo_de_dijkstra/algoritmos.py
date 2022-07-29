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
   for nodo in grafo:
      for value in grafo[nodo]:
         arista1 = (value[1], (nodo, value[0]))
         arista2 = (value[1], (value[0], nodo))
         if arista1 not in visitados and arista2 not in visitados:
            visitados.append(arista1)
            pq.put(arista1)
      disjuntos.append([nodo])

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
        
def alg_dijkstra(grafo, origen, destino):
   pq = PriorityQueue()
   distancia = dict()
   camino = dict()
   recorrido = list()

   for nodo in grafo.keys():
      distancia[nodo] = math.inf
      camino[nodo] = 0
   distancia[origen] = 0
   pq.put((0, origen))
   while not pq.empty():
      nodoOrigen = pq.get()
      nodo = nodoOrigen[1]
      adyacentes = grafo[nodo]
      for adyacente in adyacentes:
         nueva_dis = adyacente[1] + distancia[nodo]
         if nueva_dis < distancia[adyacente[0]]:
            pq.put((nueva_dis, adyacente[0]))
            distancia[adyacente[0]] = nueva_dis
            camino[adyacente[0]] = nodo
   mystr = pformat(distancia, width=40, indent=1)
   print(mystr)
   mystr = pformat(camino, width=40, indent=1)
   print(mystr)
   nodoReco = destino
   while nodoReco != origen:
      padre = camino[nodoReco]
      dife = distancia[nodoReco]
      arista = (nodoReco, padre, dife)
      recorrido.append(arista)
      nodoReco = camino[nodoReco]
   return recorrido



