import os
import math
import time
import sys
import random
import msvcrt

quantum = 0
cont_global = 0
nuevos = [] 
listos = [] 
terminados = [] 
ejecucion = [] 
bloqueados = [] 


class Lote:
    def __init__(self, id, operacion, tiempo_estimado, num1, num2, vacio):
        self.id = id
        self.operacion = operacion
        self.tiempo_estimado = tiempo_estimado
        self.num1 = num1
        self.num2 = num2
        self.error = 0
        self.tiempo_transcurrido_bloqueado  = 0
        self.tiempo_transcurrido = 0
        self.tiempo_quantum = 0
        self.tiempo_llegada = None
        self.tiempo_finalizacion = None
        self.espera = None
        self.tiempo_retorno = None
        self.tiempo_respuesta = None    
        self.vacio = vacio

    def __str__(self):
        if (not vacio):
            return (str(self.id) + " " + 
                str(self.operacion)+ " " + 
                str(self.tiempo_estimado) + " " + 
                str(self.num1)  + " " +  
                str(self.num2))
        else: 
            return " "


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
    resultado = str(num1) + " " + str(operando) + " " + str(num2) + " = " + "%.2f" %(res)
    
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


def asignar_procesos(cantidad_procesos, tiempo):

    global quantum 
    quantum = tiempo
    
    for i in range(0,cantidad_procesos):
        llenado_automatico(i)

    i = 0
    conteo = 0
    condicion = True
    
    if (len(nuevos)>5):
        cantidad_procesos = len(nuevos)
    else:
        cantidad_procesos = 6
        
    while(i<cantidad_procesos):
       
        if (i == conteo+5):
            procesar()
            conteo += 5
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
            elif(len(listos)<5):
                lote = Lote(id = 0,operacion=0,tiempo_estimado=0,num1=0,num2=0, vacio=True)
                listos.append(lote)
        i+=1
    impresion_de_tabla()
        

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

    lote = Lote(id,operacion,tiempo_estimado,num1,num2, False)
    nuevos.append(lote)
    

def procesar():
    i = 0
    long = len(nuevos)+len(listos)+len(ejecucion)
    while (len(listos)>0): 
        ejecucion.append(listos[0])
        listos.remove(listos[0])
        impresion_de_procesos()
        if (len(ejecucion)>0):
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
            while(condicion):
                if(msvcrt.kbhit()):
                    tecla = msvcrt.getwch()
                    if(tecla == 'c' or tecla == 'C'):
                        break
                    else:
                        print("Esa no es la letra c")
                continue
            salida = True


        elif(tecla == 'n' or tecla == 'N'):
            n = 0
            for lote in listos:
                if(not lote.vacio):
                    n+=1
            llenado_automatico(len(nuevos)+len(terminados)+(n)+len(ejecucion)+len(bloqueados))
            nuevos[len(nuevos)-1].tiempo_llegada = cont_global
            salida = True
                
        elif(tecla == 't' or tecla == 'T'):
            impresion_de_tabla()
            print("Presiona la letra c para continuar con el proceso: ")
            while(condicion):
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
    global quantum

    if ejecucion[0].tiempo_quantum == 0:
        ejecucion[0].tiempo_quantum = quantum

    if len(listos) >= 0:
        tiempo_transcurrido = ejecucion[0].tiempo_transcurrido
        if tiempo_transcurrido == 0:
            ejecucion[0].tiempo_respuesta = cont_global

        while(tiempo_transcurrido<=ejecucion[0].tiempo_estimado and ejecucion[0].tiempo_quantum >= 0):

            if ejecucion[0].tiempo_quantum == 0:
                listos.append(ejecucion[0])
                ejecucion.remove(ejecucion[0])
                break
            
            for i in range(len(listos)):
                if(listos[i].vacio and len(nuevos)>0):
                    listos[i] = nuevos[0]
                    nuevos.remove(listos[i])


            teclas()
            print("*********************************")
            print("Contador Global: " + str(cont_global))
            print("*********************************")
            print("Nuevos")
            print("{:<15}{:^10}".format("ID","TME"))
            if len(nuevos) > 0:
                for procesos in nuevos:
                    print("{:<15}{:^10}".format(str(procesos.id), str(procesos.tiempo_estimado)))
            print("*********************************")
            print("Listos")
            print("{:<15}{:^10}{:^10}".format("ID", "TME", "TT"))
           
            for lote in listos:
                if (lote != ejecucion[0] and lote.vacio == 0):
                    print("{:<15}{:^10}{:^10}".format(str(lote.id), str(lote.tiempo_estimado), str(lote.tiempo_transcurrido)))


            if len(ejecucion) > 0 and ejecucion[0].error != 1:
                print("*********************************")
                print("Procesos en ejecución" )
                print("{:<15}{:^10}".format("Id: ", str(ejecucion[0].id)))
                print("{:<15}{:^10}".format("Operación: ", (obtener_operacion(ejecucion[0]))))
                print("{:<15}{:^10}".format("TME: ", str(ejecucion[0].tiempo_estimado)))
                print("{:<15}{:^10}".format("TT: ", str(tiempo_transcurrido)))
                print("{:<15}{:^10}".format("TR: ", str(ejecucion[0].tiempo_estimado-tiempo_transcurrido)))
            cont_global += 1
            ejecucion[0].tiempo_quantum -= 1

            print("*********************************")
            print("Bloqueados")
            print("{:<15}{:^10}".format("ID", "TTB"))
            if(len(bloqueados) > 0):
                for lote in bloqueados:
                    if lote.tiempo_transcurrido_bloqueado  <= 7:
                        print("{:<15}{:^10}".format(str(lote.id), str(lote.tiempo_transcurrido_bloqueado )))
                        lote.tiempo_transcurrido_bloqueado  += 1
                    else:
                        lote.tiempo_transcurrido_bloqueado  = 0
                        listos.append(lote)
                        bloqueados.remove(lote)
                        
            tiempo_transcurrido += 1
            ejecucion[0].tiempo_transcurrido = tiempo_transcurrido

            print("*********************************")
            print("Terminados")
            print("{:<15}{:^10}".format("ID", "Operacion y resultado" ))
            for terminado in terminados:
                if(terminado.error == 0 and terminado.vacio == 0):
                    print("{:<15}{:^10}".format(str(terminado.id), (obtener_resultado(terminado))))
                elif(terminado.error == 1):
                    print("{:<15}{:^10}".format(str(terminado.id), "ERROR"))

            time.sleep(1)

            if(len(ejecucion) == 1 and tiempo_transcurrido>ejecucion[0].tiempo_estimado and ejecucion[0].error == 0):
                print("{:<15}{:^10}".format(str(ejecucion[0].id), (obtener_resultado(ejecucion[0]))))
                
            elif((len(ejecucion) == 1 and tiempo_transcurrido>ejecucion[0].tiempo_estimado and ejecucion[0].error != 0)):
                print("{:<15}{:^10}".format(str(ejecucion[0].id), "ERROR"))               
            os.system("cls")
            


def impresion_de_tabla():
    print('{:^10}{:^10}{:^20}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format("ID", "Est", "Operacion", "TLL", "TF", "TRet", "TEs", "TSe", "TRcpu", "Tres", "TTB"))
    print("*************************************************************************************************************************")
    for i in range(0, len(terminados)):
        if terminados[i].vacio:
            continue
        terminados[0].espera = 0
        terminados[0].tiempo_retorno = terminados[0].tiempo_transcurrido
        if terminados[i]!=terminados[0]:
            terminados[i].espera = terminados[i-1].tiempo_finalizacion
            terminados[i].tiempo_retorno = terminados[i].tiempo_finalizacion - terminados[i].tiempo_llegada

        if terminados[i].error == 0:
            print('{:^10}{:^10}{:^20}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format(str(terminados[i].id), "T", 
            str(obtener_resultado( terminados[i])), 
            str(terminados[i].tiempo_llegada), 
            str(terminados[i].tiempo_finalizacion), 
            str(terminados[i].tiempo_retorno), 
            str(terminados[i].espera), 
            str(terminados[i].tiempo_transcurrido), 
            str(terminados[i].tiempo_estimado-terminados[i].tiempo_transcurrido), 
            str(terminados[i].tiempo_respuesta)))
        elif terminados[i].error == 1:
            print('{:^10}{:^10}{:^20}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format(str(terminados[i].id), "E", "ERROR", 
            str(terminados[i].tiempo_llegada), 
            str(terminados[i].tiempo_finalizacion), 
            str(terminados[i].tiempo_retorno), 
            str(terminados[i].espera), 
            str(terminados[i].tiempo_transcurrido), 
            str(terminados[i].tiempo_estimado-terminados[i].tiempo_transcurrido), 
            str(terminados[i].tiempo_respuesta)))

    for i in range(0, len(ejecucion)):
        print('{:^10}{:^10}{:^20}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format(str(ejecucion[i].id), "E", 
        str(obtener_resultado( ejecucion[i])), 
        str(ejecucion[i].tiempo_llegada), 
        str(ejecucion[i].tiempo_finalizacion), 
        str(ejecucion[i].tiempo_retorno), 
        str(ejecucion[i].espera), 
        str(ejecucion[i].tiempo_transcurrido), 
        str(ejecucion[i].tiempo_estimado-ejecucion[i].tiempo_transcurrido), 
        str(ejecucion[i].tiempo_respuesta)))

    for i in range(0, len(bloqueados)):
        print('{:^10}{:^10}{:^20}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format(str(bloqueados[i].id), "B", 
        str(obtener_resultado( bloqueados[i])), 
        str(bloqueados[i].tiempo_llegada), 
        str(bloqueados[i].tiempo_finalizacion), 
        str(bloqueados[i].tiempo_retorno), 
        str(bloqueados[i].espera), 
        str(bloqueados[i].tiempo_transcurrido), 
        str(bloqueados[i].tiempo_estimado-bloqueados[i].tiempo_transcurrido), 
        str(bloqueados[i].tiempo_respuesta), 
        str(7 - bloqueados[i].tiempo_transcurrido_bloqueado))) 

    for i in range(0, len(listos)):
        print('{:^10}{:^10}{:^20}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format(str(listos[i].id), "L", 
        str(obtener_resultado( listos[i])), 
        str(listos[i].tiempo_llegada), 
        str(listos[i].tiempo_finalizacion), 
        str(listos[i].tiempo_retorno), 
        str(listos[i].espera), 
        str(listos[i].tiempo_transcurrido), 
        str(listos[i].tiempo_estimado-listos[i].tiempo_transcurrido), 
        str(listos[i].tiempo_respuesta))) 
        
    for i in range(0, len(nuevos)):
        print('{:^10.0f}{:^10}{:^20}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format(nuevos[i].id, "N", "null", "null", "null", "null", "null", "null", "null", "null"))
    
    errores=0
    normal=0
    n = 0
    for lote in terminados:
        if(not lote.vacio and not lote.error):
            n+=1
    print("\n")
    print("Procesos terminados: ", (n))
    print("Tiempo total en completar los procesos: " + str(cont_global))

def main():
    cantidad_procesos = int(input("Introduzca la cantidad de procesos: "))
    quantum = int(input("Numero de el quantum: "))
    asignar_procesos(cantidad_procesos, quantum)


if __name__ == "__main__":
    main()
