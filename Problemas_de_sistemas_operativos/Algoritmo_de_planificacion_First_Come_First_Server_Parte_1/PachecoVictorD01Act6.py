import os
import math
import time
import sys
import random
import msvcrt


cont_global = 0
nuevos = [] 
listos = [] 
terminados = [] 
ejecucion = [] 
bloqueados = [] 


class Lote:
    def __init__(self, id, operacion, tiempo_estimado, num1, num2):
        self.id = id
        self.operacion = operacion
        self.tiempo_estimado = tiempo_estimado
        self.num1 = num1
        self.num2 = num2
        self.error = 0
        self.tiempo_transcurrido_bloqueado  = 0
        self.tiempo_transcurrido = 0
        self.tiempo_llegada = 0
        self.tiempo_finalizacion = 0
        self.espera = 0
        self.tiempo_retorno = 0
        self.tiempo_respuesta = 0      

    def __str__(self):
        return (str(self.id) + " " + 
            str(self.operacion)+ " " + 
            str(self.tiempo_estimado) + " " + 
            str(self.num1)  + " " +  
            str(self.num2))


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


def asignar_procesos(cantidad_procesos):
    
    for i in range(0,cantidad_procesos):
        llenado_automatico(i)

    i = 0
    conteo = 0
    condicion = True
    cantidad_procesos = len(nuevos)

    while(i<cantidad_procesos):
        if (i == conteo + 5):
            procesar()
            conteo += 1
            if (len(nuevos) > 0 and condicion):    
                nuevos[0].tiempo_llegada = cont_global
                listos.append(nuevos[0])
                nuevos.remove (nuevos[0])
                listos[0].tiempo_respuesta = cont_global
                condicion = False
            if (len(listos) == 1):
                ejecucion.append(listos[0])
                listos.remove(listos[0])
                impresion_de_procesos()
        else:
            if (len(nuevos) > 0):
                nuevos[0].tiempo_llegada = cont_global
                listos.append(nuevos[0])
                nuevos.remove(nuevos[0])
        i+=1

    

    if (len(terminados) == cantidad_procesos):
        errores=0
        normal=0
        print("Procesos terminados: ", len(terminados))

        for i in range(len(terminados)):
            errores += terminados[i].error
        print("Procesos terminados en error: "+ str(errores))

        print("ID" +("{:10}".format(''))+ 
        "Llegada" +("{:8}".format(''))+ 
        "Finalizacion" +("{:6}".format(''))+
        "Espera" +("{:10}".format(''))+
        "Servicio" +("{:8}".format(''))+
        "Retorno" +("{:8}".format(''))+
        "Respuesta" + ("{:8}".format('')+ 
        "Terminado"))
        print("************************************************************************************************************************")
        for i in range(0,len(terminados)):
            terminados[i].tiempo_retorno = terminados[i].tiempo_finalizacion - terminados[i].tiempo_llegada
            terminados[i].espera = terminados[i].tiempo_retorno - terminados[i].tiempo_transcurrido
            print(str(terminados[i].id) +"\t\t"+ 
                str(terminados[i].tiempo_llegada) +"\t\t" + 
                str(terminados[i].tiempo_finalizacion) +"\t\t"+ 
                str(terminados[i].espera) +"\t\t"+ 
                str(terminados[i].tiempo_transcurrido) +"\t\t"+ 
                str(terminados[i].tiempo_retorno)+"\t \t"+ 
                str(terminados[i].tiempo_respuesta)+"\t \t"+ 
                "Error" * (terminados[i].error) + "Normal"* (not terminados[i].error))
        

def llenado_automatico(i):
    os.system("cls")
    id = i+1
    num1 = (random.randrange(0, 100))
    num2 = (random.randrange(0, 100))
    operacion = (random.randrange(1, 5))
    tiempo_estimado = (random.randrange(6, 16))

    if((operacion == 4 or operacion == 5) and num2 == 0):
        num2 = (random.randrange(1, 100))
        continuar = (num2==0)

    lote = Lote(id,operacion,tiempo_estimado,num1,num2)
    nuevos.append(lote)
    

def procesar():
    i = 0
    long = len(listos)
    while (i<=long and len(listos) > 0): 
        ejecucion.append(listos[0])
        listos.remove(listos[0])
        impresion_de_procesos()
        ejecucion[0].tiempo_finalizacion = cont_global
        terminados.append(ejecucion[0])
        if (len(nuevos) > 0):
            nuevos[0].tiempo_llegada = cont_global
            listos.append(nuevos[0])
            nuevos.remove(nuevos[0])
        ejecucion.remove(ejecucion[0])
        i+=1
        

def teclas():
    salida = False
    condicion = True
    if(msvcrt.kbhit()):
        tecla = msvcrt.getwch()
        if(tecla == 'i' or tecla == 'I'):
            if len(listos) > 0 and len(bloqueados) < 3:        
                bloqueados.append(ejecucion[0])
                ejecucion.remove(ejecucion[0])
                ejecucion.append(listos[0])
                listos.remove(listos[0])
                impresion_de_procesos()
            salida = True

        elif(tecla == 'e' or tecla == 'E'):
            ejecucion[0].tiempo_estimado = 0
            ejecucion[0].error = 1
            salida = True

        elif(tecla == 'p' or tecla == 'P'):
            print("Presiona la letra c para continuar con el proceso: ")
            while(True):
                if(msvcrt.kbhit()):
                    tecla = msvcrt.getwch()
                    if(tecla == 'c' or tecla == 'C'):
                        break
                    else:
                        print("Esa no es la letra c")
                continue
            salida = True

    return salida
        

def impresion_de_procesos():

    global cont_global

    if len(listos) >= 0:
        tiempo_transcurrido = ejecucion[0].tiempo_transcurrido
        if tiempo_transcurrido == 0:
            ejecucion[0].tiempo_respuesta = cont_global
        while(tiempo_transcurrido<=ejecucion[0].tiempo_estimado):

            teclas()
            
            print("*********************************")
            print("Contador Global: " + str(cont_global))
            print("*********************************")
            print("Nuevos")
            print("ID" +("{:14}".format('')+"TME"))
            if len(nuevos) > 0:
                for procesos in nuevos:
                    print(str(procesos.id) +("{:15}".format('')+ str(procesos.tiempo_estimado)))
            print("*********************************")
            print("Listos")
            print("ID" +("{:14}".format('')+"TME" +("{:13}".format('')+ "TT")))
           
            for lote in listos:
                if (lote != ejecucion[0]):
                    print(str(lote.id) + ("{:15}".format('') + 
                    str(lote.tiempo_estimado) + ("{:15}".format('') + 
                    str(lote.tiempo_transcurrido))))

            if len(ejecucion) > 0 and ejecucion[0].error != 1:
                print("*********************************")
                print("Procesos en ejecución" )
                print("Id: " +("{:12}".format('')+ str(ejecucion[0].id)))
                print("Operación: " +("{:5}".format('')+ str(obtener_operacion(ejecucion[0]))))
                print("TME: " +("{:11}".format('')+ str(ejecucion[0].tiempo_estimado)))
                print("TT: " +("{:12}".format('')+ str(tiempo_transcurrido)))
                print("TR: " +("{:12}".format('')+ str(ejecucion[0].tiempo_estimado-tiempo_transcurrido)))
            cont_global += 1

            print("*********************************")
            print("Bloqueados")
            print("ID" +("{:14}".format('')+ "TTB"))
            if(len(bloqueados) > 0):
                for lote in bloqueados:
                    if lote.tiempo_transcurrido_bloqueado  <= 7:
                        print(str(lote.id) + ("{:15}".format('') + str(lote.tiempo_transcurrido_bloqueado )))
                        lote.tiempo_transcurrido_bloqueado  += 1
                    else:
                        lote.tiempo_transcurrido_bloqueado  = 0
                        listos.append(lote)
                        bloqueados.remove(lote)
                        
            tiempo_transcurrido += 1
            ejecucion[0].tiempo_transcurrido = tiempo_transcurrido

            print("*********************************")
            print("Terminados")
            print("ID" +("{:14}".format('')+ "Operacion" ))
            for terminado in terminados:
                if(terminado.error == 0):
                    print(str(terminado.id) +("{:15}".format('')+ str(obtener_resultado(terminado))))
                elif(terminado.error == 1):
                    print(str(terminado.id) +("{:15}".format('')+ "ERROR "))

            time.sleep(1)

            if(len(ejecucion) == 1 and tiempo_transcurrido>ejecucion[0].tiempo_estimado and ejecucion[0].error == 0):
                print(str(ejecucion[0].id) + "\t\t\t| " + str(obtener_resultado(ejecucion[0])))
                
            elif((len(ejecucion) == 1 and tiempo_transcurrido>ejecucion[0].tiempo_estimado and ejecucion[0].error != 0)):
                print(str(ejecucion[0].id) +  "\t\t\t| ERROR ")               
            os.system("cls")


def main():
    cantidad_procesos = int(input("Introduzca la cantidad de procesos: "))
    asignar_procesos(cantidad_procesos)


if __name__ == "__main__":
    main()
