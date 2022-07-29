import os
import math
import time
import sys

cont_global = 0
cantidad_lotes = []
lotes_terminados = []

class Lote:
    def __init__(self, id, nombre, operacion, tiempo_estimado, num1, num2, num_lote):
        self.id = id
        self.nombre = nombre
        self.operacion = operacion
        self.tiempo_estimado = tiempo_estimado
        self.num1 = num1
        self.num2 = num2
        self.num_lote = num_lote

    def __str__(self):
        return ( str(self.id) + " " + self.nombre + " " 
        + str(self.operacion  )+ " " + str(self.tiempo_estimado) 
        + " " + str(self.num1)  + " " +  str(self.num2) + " "+ str(self.num_lote) + " ")

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
    num_procesos = len(cantidad_lotes)
    numlotes = int(num_procesos/5)
    if(num_procesos % 5 > 0):
        numlotes += 1
    return numlotes

def validar_tiempo():
    continuar = True
    while continuar:
        tiempo_estimado = int(input("TME: "))
        if (tiempo_estimado > 0):
            continuar = False
        else:
            print("El tiempo tiene que ser mayor que 0")
    return tiempo_estimado

def procesar(num_lote, lote_actual,cant_lotes):
    i = 0
    long = len(lote_actual)
    while (i<long):
        ejecucion_de_lotes(num_lote,lote_actual,cant_lotes)
        lote_actual.remove(lote_actual[0])
        i+=1


def asignar_procesos(cantidad_procesos):
    num_lotes = 1
    conteo = 0

    for i in range(0,cantidad_procesos):
        if(i==conteo+5):
            num_lotes+=1
            conteo+=5
            obtener_datos(num_lotes)
            os.system("cls")
        else:
            obtener_datos(num_lotes)
            os.system("cls")

    lote_actual = []
    num_lotes = 1
    conteo = 0
    cant_lotes = numero_lotes()
    cantidad_procesos = len(cantidad_lotes)

    for i in range(0, cantidad_procesos):
        if (i == conteo + 5):
            procesar(num_lotes, lote_actual, cant_lotes)
            num_lotes += 1
            conteo += 5
            lote_actual.clear()
            lote_actual.append(cantidad_lotes[i])
        else:
            lote_actual.append(cantidad_lotes[i])
    if (cant_lotes - num_lotes == 0 and i + 1 == cantidad_procesos):
        procesar(num_lotes, lote_actual,cant_lotes)


def verificar_id():
    continuar = True
    while continuar:
        id = int(input("ID: "))
        if (id > 0 and buscar_id(id)==False):
            continuar = False
        else:
            print("ID no se puede repetir ")
    return id

def buscar_id(id):
    if(len(cantidad_lotes)==0):
        return False
    for lote in cantidad_lotes:
        if (lote.id == id):
            return True
    return False


def obtener_datos(num_lotes):
    os.system("cls")
    nombre = input("Nombre: ")
    id = verificar_id()
    tiempo_estimado = validar_tiempo()
    operacion = menu_operaciones()
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    continuar = True
    if((operacion == 4 or operacion == 5) and num2 == 0):
        while continuar:
            print("Tiene que ser un numero mayor a 0")
            num2 = int(input("Numero 2: "))
            continuar = (num2==0)
    lote = Lote(id,nombre,operacion,tiempo_estimado,num1,num2, num_lotes)
    cantidad_lotes.append(lote)

def ejecucion_de_lotes(num_lote,lote_actual,cant_lotes):

    global cont_global  
    tiempo_total = 0
    while(tiempo_total<=lote_actual[0].tiempo_estimado):
        
        for lote in lote_actual:
            if (lote != lote_actual[0]):
                print("Id de proceso|Tiempo estimado")
                print(str(lote.id) + "\t\t" + str(lote.tiempo_estimado))
        print("*********************************")
        print("Numero de Lotes pendientes: " + str(cant_lotes - num_lote))
        print("Lote en ejecución: " + str(num_lote))
        print("Contador Global: " + str(cont_global))
        print("*********************************")
        print("Lotes en ejecución" )
        print("Nombre: " + str(lote_actual[0].nombre))
        print("Operación: " + str(obtener_operacion(lote_actual[0])))
        print("ID: " + str(lote_actual[0].id))
        print("TME: " + str(lote_actual[0].tiempo_estimado))
        print("TT: " + str(tiempo_total))
        print("TR: " + str(lote_actual[0].tiempo_estimado-tiempo_total)) 
        cont_global += 1
        tiempo_total += 1
        print("*********************************")
        print("Lotes terminados")
        print("ID \t| NL \t|Operacion y resultado" )
        for terminado in lotes_terminados:
            print(str(terminado.id) + "\t| " + str(terminado.num_lote) + "\t| " 
            + str(obtener_resultado(terminado)))
        time.sleep(1)
        if(cant_lotes - num_lote == 0 and len(lote_actual) == 1 and tiempo_total>lote_actual[0].tiempo_estimado):
            print(str(lote_actual[0].id) + "\t| " + str(lote_actual[0].num_lote) 
            + "\t| " + str(obtener_resultado(lote_actual[0])))
            os.system("pause")
        os.system("cls")
    lotes_terminados.append(lote_actual[0])

procesar_lotes = int(input("Introduzca la cantidad de procesos: "))
asignar_procesos(procesar_lotes)

