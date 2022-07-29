import os
import math
import time
import sys
import random
import msvcrt
         
tiempo_transcurrido = 0
cont_global = 0
ejecutar_lotes = []
lotes_terminados = []
lote_actual = []


class Lote:
    def __init__(self, id, operacion, tiempo_estimado, num1, num2, num_lote):
        self.id = id
        self.operacion = operacion
        self.tiempo_estimado = tiempo_estimado
        self.num1 = num1
        self.num2 = num2
        self.num_lote = num_lote
        self.tiempo_transcurrido = 0
        self.error = 0

    def __str__(self):
        return ( str(self.id) 
            + " " + str(self.operacion)
            + " " + str(self.tiempo_estimado) 
            + " " + str(self.num1) 
            + " " + str(self.num2) 
            + " " + str(self.num_lote)
            + " " + str(self.tiempo_transcurrido))


def menu_operaciones():
    print("Operación")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    print("5) Residuo")
    operacion = 0 
    while(operacion == 0):
        operacion = int(input("Introduce la opcion: "))
        if operacion < 6 and operacion > 0:
            return operacion 
    else: 
        operacion = 0


def obtener_resultado(lote):
    num1 = lote.num1
    num2 = lote.num2
    operacion = lote.operacion
    res = 0
    operando = ''
    if(operacion == 1):
        res = num1 + num2
        operando = '+'
    elif(operacion == 2):
        res = num1 - num2
        operando = '-'
    elif (operacion == 3):
        res = num1 * num2
        operando = '*'
    elif (operacion == 4):
        res = num1 / num2
        operando = '/'
    elif (operacion == 5):
        res = num1 % num2
        operando = '%'
    resultado = str(num1) + " " + str(operando) + " " + str(num2) + " = " + str(res)
    
    return resultado


def obtener_operacion(lote):
    num1 = lote.num1
    num2 = lote.num2
    operacion = lote.operacion
    res = 0
    operando = ''
    if(operacion == 1):
        res = num1 + num2
        operando = '+'
    elif(operacion == 2):
        res = num1 - num2
        operando = '-'
    elif (operacion == 3):
        res = num1 * num2
        operando = '*'
    elif (operacion == 4):
        res = num1 / num2
        operando = '/'
    elif (operacion == 5):
        res = num1 % num2
        operando = '%'
    resultado = str(num1) + " " + str(operando) + " " + str(num2) 
    
    return resultado


def numero_lotes():
    num_procesos = len(ejecutar_lotes)
    numlotes = int(num_procesos/5)
    if(num_procesos % 5 > 0):
        numlotes += 1
    return numlotes


def procesar(num_lote, lote_actual,cant_lotes):
    i = 0
    long = len(lote_actual)
    while (i<long):
        ejecucion_de_lotes(num_lote,cant_lotes)
        lotes_terminados.append(lote_actual[0])
        lote_actual.remove(lote_actual[0])
        i+=1


def asignar_procesos(cantidad_procesos):
    num_lotes = 1
    conteo = 0

    for i in range(0,cantidad_procesos):
        if(i==conteo+5):
            num_lotes+=1
            conteo+=5
            llenado_automatico(num_lotes,i)
        else:
            llenado_automatico(num_lotes, i)

    num_lotes = 1
    conteo = 0
    cant_lotes = numero_lotes()
    cantidad_procesos = len(ejecutar_lotes)
    for i in range(0, cantidad_procesos):
        if (i == conteo + 5):
            procesar(num_lotes, lote_actual,cant_lotes)
            num_lotes += 1
            conteo += 5
            lote_actual.clear()
            lote_actual.append(ejecutar_lotes[i])
        else:
            lote_actual.append(ejecutar_lotes[i])
    
    if (cant_lotes - num_lotes == 0 and i + 1 == cantidad_procesos):
        procesar(num_lotes, lote_actual,cant_lotes)


def llenado_automatico(num_lotes,i):
    os.system("cls")
    id = i+1
    num1 = (random.randrange(0, 100))
    num2 = (random.randrange(0, 100))
    operacion = (random.randrange(1, 5))
    tiempo_estimado = (random.randrange(6, 16))

    if((operacion == 4 or operacion == 5) and num2 == 0):
        num2 = (random.randrange(1, 100))
        continuar = (num2==0)
        
    lote = Lote(id,operacion,tiempo_estimado,num1,num2, num_lotes)
    ejecutar_lotes.append(lote)


def teclas(num_lote, cant_lotes, tiempo):
    salida = False
    condicion = True
    if msvcrt.kbhit():
        tecla = msvcrt.getwch()
        if(tecla == 'i' or tecla == 'I'):
            lote_actual[0].tiempo_estimado = tiempo
            lote_actual.append(lote_actual[0])
            lote_actual.remove(lote_actual[0])
            ejecucion_de_lotes(num_lote, cant_lotes)
            salida = True

        elif(tecla == 'e' or tecla == 'E'):
            lote_actual[0].tiempo_estimado = 0
            lote_actual[0].error = 1
            salida = True

        elif(tecla == 'p' or tecla == 'P'):
            while(condicion):
                c = input("Presiona la letra c para continuar con el proceso: ")
                if(c == "c" or c == "C"):
                    break
                else:
                    print("Esa no es la letra c")
                continue
            salida = True

    return salida


def ejecucion_de_lotes(num_lote, cant_lotes):

    global cont_global
    tiempo_transcurrido = 0

    while(tiempo_transcurrido<=lote_actual[0].tiempo_estimado):  
        
        if teclas(num_lote, cant_lotes, lote_actual[0].tiempo_estimado-tiempo_transcurrido):
            break
        
        os.system("cls")
        for lote in lote_actual:
            if (lote != lote_actual[0] and lote.id):
                print("Id de proceso|Tiempo estimado|Tiempo transcurrido")
                print(str(lote.id) + "\t\t" + str(lote.tiempo_estimado)+ "\t\t" + str(lote.tiempo_transcurrido))
                
        print("*********************************")
        print("Numero de Lotes pendientes: " + str(cant_lotes - num_lote))
        print("Lote en ejecución: " + str(num_lote))
        print("Contador Global: " + str(cont_global))
        print("*********************************")
        print("Lotes en ejecución" )
        print("Operación: " + str(obtener_operacion(lote_actual[0])))
        print("ID: " + str(lote_actual[0].id))
        print("TME: " + str(lote_actual[0].tiempo_estimado))
        print("TT: " + str(tiempo_transcurrido))
        print("TR: " + str(lote_actual[0].tiempo_estimado-tiempo_transcurrido)) 
        cont_global += 1
        tiempo_transcurrido += 1
        lote_actual[0].tiempo_transcurrido=tiempo_transcurrido
        print("*********************************")
        print("Lotes terminados")
        print("ID \t| NL \t|Operacion y resultado" )

        for terminado in lotes_terminados:
            if(terminado.error == 0):
                print(str(terminado.id) + "\t| " 
                + str(terminado.num_lote) + "\t| " 
                + str(obtener_resultado(terminado)))
            elif(terminado.error == 1):
                print(str(terminado.id) +  "\t| ERROR")
        time.sleep(1)

        if(cant_lotes - num_lote == 0 and len(lote_actual) == 1 
            and tiempo_transcurrido>lote_actual[0].tiempo_estimado and lote_actual[0].error == 0):
            print(str(lote_actual[0].id) + "\t| " 
            + str(lote_actual[0].num_lote) + "\t| " 
            + str(obtener_resultado(lote_actual[0])))
            os.system("pause")

        elif((cant_lotes - num_lote == 0 and len(lote_actual) == 1 
            and tiempo_transcurrido>lote_actual[0].tiempo_estimado and lote_actual[0].error != 0)):
            print(str(lote_actual[0].id) + "\t| ERROR ")

        os.system("cls")


def main():
    cantidad_lotes = int(input("Introduzca la cantidad de trabajos a procesar: "))
    asignar_procesos(cantidad_lotes)


if __name__ == "__main__":
    main()

