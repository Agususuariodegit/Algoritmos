import math 

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

# def tiene_vocales_dis(palabra:str) -> bool:
#     res = bool
#     vocales_dis: list [str] = ""  
#     for i in range(0,len(palabra),1):
#         if (97 <= ord(palabra[i]) and ord(palabra[i]) <= 122):
#             vocales_dis += palabra[i]




