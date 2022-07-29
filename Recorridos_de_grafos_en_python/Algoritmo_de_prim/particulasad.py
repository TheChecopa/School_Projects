from particula import Particula
from queue import PriorityQueue
from pprint import pformat
from collections import deque
import json

class Particulasad:
    def __init__(self):

        self.__particulas = []

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)


    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent=5)
                return 1
        except:
            return 0 

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, "r") as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
                return 1

        except:
            return 0

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration

            
    def ordenar_id(self):
        self.__particulas.sort()

    def ordenar_distancia(self):
        self.__particulas.sort(key=lambda particula: particula.distancia, reverse=True)

    def ordenar_velocidad(self):
        self.__particulas.sort(key=lambda particula: particula.velocidad)
    

    #def sort_by_id(self):
    #    self.__particulas.sort()
    
    #def sort_by_distancia(self):
    #    self.__particulas.sort(key=lambda particula: particula.distancia, reverse=True)

    #def sort_by_velocidad(self):
    #    self.__particulas.sort(key=lambda particula: particula.velocidad)
            
        
#p01 = Particula(id=10, origen_x=3, origen_y=6, destino_x=4, destino_y=8, velocidad=20, red=2, green=3, blue=4)
#p02 = Particula(id=20, origen_x=4, origen_y=8, destino_x=9, destino_y=18, velocidad=30, red=5, green=6, blue=7)
#particulasad = Particulasad()
#particulasad.agregar_inicio(p01)
#particulasad.agregar_final(p02)
#particulasad.mostrar()


