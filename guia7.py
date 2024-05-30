from typing import List, Dict, Tuple
import math 
import random

# Primera parte

def pertenece(x:int, lista: list [int]) -> bool:
    contador:int = 0
    res:bool = False 
    while (contador < len(lista)):
        if (lista[contador] == x):
            res = True
            contador = len(lista) + 1 
        else:
            contador += 1 
    return res

def divide_a_todos(x:int, lista: list [int]) -> bool:
    contador:int = 0
    res:bool = True
    divisores:int = 0 
    while (contador < len(lista)):
        if (lista [contador] % x == 0):
             divisores += 1
             contador += 1  
        else:
            contador += 1 
    if (divisores == len(lista)):
        res = True 
    else:
        res = False 
    return res 

def suma_total(lista: list [int]) -> int:
    indice:int = 0
    suma: int = 0 
    while (indice < len(lista)):
        suma += lista [indice]
        indice += 1 
    return suma 

def ordenados(lista: list[int]) -> bool:
    i:int = 0 
    res:bool = True 
    while (i < len(lista) - 1):
        if (lista[i] <= lista[i + 1]):
            i += 1 
        else:
            res = False
            i += 1  
    return res 

def alguna_palabra(lista: list[str]) -> bool:
    i:int = 0
    res:bool = False 
    while (i < len(lista)):
        if (len (lista[i]) > 7):
            res = True 
            i += 1 
        else:
            i += 1 
    return res 

# Ejercicio 6

def es_palindromo(palabra:str) -> bool:
    res:bool = reverso(palabra) == palabra
    return res 

def reverso(palabra:str) -> str:
    a:str = ""
    for i in range (len(palabra)-1,-1,-1):
        a += palabra[i]
    return a

# Ejercicio 7

def hay_minusculas(palabra:str) -> bool:
    res:bool = False 
    for i in range (0,len(palabra),1):
        if (97 <= ord(palabra[i]) and ord(palabra[i]) <= 122):
            res = True  
    return res 

        
def hay_mayusculas(palabra:str) -> bool:
    res:bool = False 
    for i in range (0,len(palabra),1):
        if (65 <= ord(palabra[i]) and ord(palabra[i]) <= 90):
            res = True  
    return res 

def hay_numeros(palabra:str) -> bool:
    res:bool = False 
    for i in range (0,len(palabra),1):
        if (48 <= ord(palabra[i]) and ord(palabra[i]) <= 57):
            res = True  
    return res 

def determinar_contraseña(contraseña:str) -> str:
    res:str = ""
    if(hay_minusculas(contraseña) and hay_mayusculas(contraseña) and hay_numeros(contraseña) and len(contraseña) > 8):
        res = "VERDE"
    else:
        if(len(contraseña) < 5):
            res = "ROJA"
        else:
            res = "AMARILLA"
    return res 

# Ejercicio 8 Anotación: los parametros in inout out no se devuelven.

def saldo_disponible(transacciones:list[tuple]) -> float:
    monto:float = 0
    for i in range(0,len(transacciones),1):
        if ((transacciones[i])[0] == "I"):
            monto += (transacciones[i])[1]
        else:
            monto -= (transacciones[i])[1]
    return monto

def tres_vocales_distintas(palabra:str) -> bool:
    res:bool = False
    vocal:str = ""
    contador:int = 0
    for i in range(0,len(palabra),1):
        if (97 <= ord(palabra[i]) and ord(palabra[i]) <= 122 and vocal != palabra[i]):
                vocal = palabra[i]
                contador += 1 
    res = contador > 2 
    return res 
            
# Segunda Parte 

# Ejercicio 2 

def poner_ceros(lista:list [int]) -> list [int]:
    for i in range(0,len(lista),1):
        lista[i] = 0 
    return lista 

def ceros_en_pares(lista:list [int]) -> list [int]:
    lista1 = lista.copy()                          
    for i in range (0,len(lista1),2):
        lista1[i] = 0
    return lista1

def caracter_pertenece(c:str, palabra:list [str]) -> bool:
    res:bool = False 
    for i in range(0,len(palabra),1):
        if (palabra[i] == c):
            res = True
    return res

def quitar_vocales(palabra:str) -> str:                                
    vocales:list [str] = ["a","e","i","o","u","A","E","I","O","U"]
    palabraNueva:str = ""
    for i in range(0,len(palabra),1):
        if (not caracter_pertenece(palabra[i],vocales)):
            palabraNueva += palabra[i]
    return palabraNueva 

def reemplazar_vocales(palabra:str) -> str:
    vocales:list [str] = ["a","e","i","o","u","A","E","I","O","U"] 
    palabraNueva:str = ""
    for i in range(0,len(palabra),1):
        if (not caracter_pertenece(palabra[i],vocales)):
            palabraNueva += palabra[i]
        else:
            palabraNueva += "_"
    return palabraNueva 

def da_vuelta_str(palabra:str) -> str:
    a = ""
    for i in range(len(palabra)-1,-1,-1):
        a += palabra[i]
    return a

def eliminar_repetidos(palabra:str) -> str:
    a = ""
    for i in range(0,len(palabra),1):
        if (not caracter_pertenece(palabra[i],a)):
            a += palabra[i]
    return a

# Ejercicio 3

def promedio(numeros:list [int]) -> int:
    res:int = suma_total(numeros)/len(numeros)
    return res

def aprobado(notas:list [int]) -> int:
    res = 0
    aprobadas:int = 0
    for i in range(0,len(notas),1):
        if(notas[i] < 4):
            res = 1
    for i in range(0,len(notas),1):
        if(notas[i] >= 4):
            aprobadas += 1 
    if (aprobadas == len(notas) and 4 <= promedio(notas) and promedio(notas) < 7):
        res = 2
    else:
        if(aprobadas == len(notas) and promedio(notas) >= 7):
            res = 3 
    return res 

# Anotaciones guia 7

# a = input("Hola, inserte algo: ")

# print(a)

# print(int(a)+9)

# Anotaciones guia 8

# archivo = open("miarchivo.txt")
# contenido = archivo.read
# contenido -> muestra el archivo sin saltos de linea
# print(contenido) -> muestra el archivo con saltos de linea 

# vi tres.txt

# def contar_lineas(nombre_archivo: str) -> int:


# Ejercicio 4

def estudiantes() -> list[str]:
    lista: list[str] = ""
    a = input("Ingrese estudiante: ")
    while( a != "listo"):
        lista += a 
        a = input("ingrese el siguiente: ")
    return lista 

def operaciones_SUBE() -> list[tuple]:
    lista_operaciones: list[tuple] = []
    operacion = input("Seleccione C, D o X: ")
    while (operacion != "X"):
        monto = input("Ingrese monto: ")
        lista_operaciones += [(operacion,monto)]
        operacion = input("Seleccione C, D o X: ")
    return lista_operaciones


def jugar_7_y_medio():

    puntaje:float = 0 
    carta = random.choice([1,2,3,4,5,6,7,10,11,12])

    if(carta == 10 or carta == 11 or carta == 12):
        puntaje += 0.5 
    else:
        puntaje += carta 
    print("Se reparte una carta \nTu carta es " + str(carta))
    print("Tu puntaje es " + str(puntaje))

    siguiente = "SI"

    while (siguiente != "NO" and puntaje < 7.50):   
            
            siguiente = input("¿Desea tomar otra carta?: ")      
            
            if (siguiente != "NO"):

                carta = random.choice([1,2,3,4,5,6,7,10,11,12])
                
                if(carta == 10 or carta == 11 or carta == 12):
                    puntaje += 0.5
                    print("Tu carta es " + str(carta))
                    print("Tu puntaje es " + str(puntaje))
                else:
                    puntaje += carta
                    print("Tu carta es " + str(carta))
                    print("Tu puntaje es " + str(puntaje))
                
    if (puntaje == 7.50):
        print("ganaste")
    else:
        print("el triplehijueputa del menor")

# Ejercicio 5 

def pertenece_a_cada_uno_version_1(lista:list [list [int]],x:int) -> list[bool]:
    res:list[bool] = []
    for i in range(0,len(lista),1):
        if(pertenece(x,lista[i])):
            res += [True]
        else:
            res += [False]
    return res 

# def problema_pertenece_a_cada_uno_version_2()

def pertenece_a_lista(x:list, lista: list [list]) -> bool:
    contador:int = 0
    res:bool = False 
    while (contador < len(lista)):
        if (lista[contador] == x):
            res = True
            contador = len(lista) + 1 
        else:
            contador += 1 
    return res

def es_matriz(lista: list[list [int]]) -> bool:
    res:bool = True
    if(lista == [] or pertenece_a_lista([],lista)):
        res = False 
    else:
        for i in range(1,len(lista),1):
            if(len(lista[i]) != len(lista[0])):
                res = False 
    return res 

def filas_ordenadas(lista: list[list [int]]) -> list[bool]:
    ordenes = []
    for i in range(0,len(lista),1):
        if(ordenados(lista[i]) == True):
            ordenes += [True]
        else:
            ordenes += [False]
    return ordenes

# import numpy as np

# d = 2
# m = np.random.randint(0,10, (d, d))

# def aplanar (matriz: list [list [int]]) -> list [list[int]]:
#     lista_vacia: list [list [int]] = []
#     for i in range(0,len(matriz),1):
#         lista_vacia += matriz[i]
#     return lista_vacia

# print(aplanar(m))





