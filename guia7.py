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

    siguiente = input("¿Desea tomar otra carta?: ")
    
    while (siguiente != "NO"):
             
             carta = random.choice([1,2,3,4,5,6,7,10,11,12])

             if(carta == 10 or carta == 11 or carta == 12):
                 puntaje += 0.5
                 print("Tu carta es " + str(carta))
                 print("Tu puntaje es " + str(puntaje))
             else:
                 puntaje += carta
                 print("Tu carta es " + str(carta))
                 print("Tu puntaje es " + str(puntaje))

print(jugar_7_y_medio())




