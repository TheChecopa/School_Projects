import time
import random
import msvcrt
import os

contenedor = []


def contenedor_vacio():
    cont = 0
    for i in range(20):
        if(contenedor[i] == "-"):
            cont += 1
    if(cont == 20):
        return True


def contenedor_lleno():
    cont = 0
    for i in range(20):
        if(contenedor[i] == "x"):
            cont += 1
    if(cont == 20):
        return True


def main():

    buffer_consumidor = 0
    buffer_productor = 0
    Verdadero = True

    for i in range(20):
        contenedor.append("-")

    while Verdadero:

        volado = random.randint(0, 1)
        productor = random.randint(2, 5)
        consumidor = random.randint(2, 5)

        if(msvcrt.kbhit()):
            tecla = msvcrt.getwch()
            if(tecla == chr(27)):
                print("Usted ha salido del programa con la letra ESC")
                break

        if(volado == 0):
            for i in range(productor):
                if buffer_productor + 1 > 19:
                    siguiente = 0
                else:
                    siguiente = buffer_productor + 1
                if len(contenedor) == 20 and contenedor_lleno() != True and contenedor[siguiente] == "-":
                    contenedor[buffer_productor] = "x"
                    buffer_productor += 1
                    if(buffer_productor == 20):
                        buffer_productor = 0

                    print("Le toco al productor", productor, "veces")
                    for i in range(20):
                        print(contenedor[i], end=" ")

                    time.sleep(2)
                    os.system('cls')

        if(volado == 1):
            for i in range(consumidor):
                if buffer_consumidor + 1 > 19:
                    siguiente = 0
                else:
                    siguiente = buffer_consumidor + 1
                if len(contenedor) == 20 and contenedor_vacio() != True and (contenedor[siguiente] == "x" or contenedor[siguiente + 1] == "-"):
                    contenedor[buffer_consumidor] = "-"
                    buffer_consumidor += 1
                    if(buffer_consumidor == 20):
                        buffer_consumidor = 0

                    print("Le toco al consumidor", consumidor, "veces")
                    for i in range(20):
                        print(contenedor[i], end=" ")

                    time.sleep(2)
                    os.system('cls')


if __name__ == "__main__":
    main()
