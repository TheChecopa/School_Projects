import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):
   dx = (x_2 - x_1)**2
   dy = (y_2 - y_1)**2
   distancia = math.sqrt((dx + dy))
   return distancia