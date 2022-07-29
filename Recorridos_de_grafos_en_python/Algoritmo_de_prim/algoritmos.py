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
         
        



