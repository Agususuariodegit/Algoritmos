# archivo = open("miarchivo.txt")
# contenido = archivo.read
# contenido -> muestra el archivo sin saltos de linea
# print(contenido) -> muestra el archivo con saltos de linea 

# vi tres.txt

# def contar_lineas(nombre_archivo: str) -> int:

from queue import LifoQueue as Pila
import random
import typing 

# Archivos 

# Ejercicio 1 

def leer_lineas(nombre_archivo:str) -> list[str]:
    archivo = open(nombre_archivo) 
    lineas: list[str] = archivo.readlines()
    archivo.close()
    return lineas

def contar_lineas(nombre_archivo:str) -> int:
    res:int = len(leer_lineas(nombre_archivo))
    return res

# print(leer_lineas("archivo.txt"))

# def pertenece_palabra(palabra:str,texto: list[str]) -> bool:
#     res:bool = False 
#     for i in range(0,len(texto),1):
#         if(texto[i] == palabra):
#             res = True
#     return res 

def leer(nombre_archivo:str):
    archivo = open(nombre_archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido 

def existe_palabra(nombre_archivo:str, palabra:str) -> bool:
    res:bool = False 
    archivo:str = leer(nombre_archivo)
    if archivo.count(palabra) > 0:
        res = True
    return res 

def cantidad_de_apariciones(nombre_archivo:str, palabra:str) -> int:
    res:int = 0
    archivo:str = leer(nombre_archivo)
    res = archivo.count(palabra)
    return res 

# Ejercicio 2 

def es_comentario(linea:str) -> bool:
    i = 0
    while i < len(linea) and linea[i] == " ":
        i += 1 
    return i < len(linea) and linea[i] == "#"  

def clonar_sin_comentarios(nombre_archivo:str):
    archivo = open(nombre_archivo,"r")
    copia = open("copia.txt","w")
    lineas = archivo.readlines()
    for i in range(0,len(lineas),1):
        if (not(es_comentario(lineas[i]))):       
            copia.write(lineas[i])
    archivo.close()
    copia = open("copia.txt")
    contenido = copia.read()
    print(contenido)    

# clonar_sin_comentarios("archivo.txt")

def invertir_lineas(nombre_archivo:str): 
    archivo = open(nombre_archivo,"r")
    copia = open("copia.txt","w")
    lineas = archivo.readlines()
    for i in range(len(lineas)-1,-1,-1):
        copia.write(lineas[i])
    archivo.close()
    copia = open("copia.txt")
    contenido = copia.read()
    print(contenido)

def linea_al_final(nombre_archivo:str, frase:str):
    
    archivo = open(nombre_archivo,"r")
    copia = open("copia.txt","w")
    lineas = archivo.readlines()

    for i in range(0,len(lineas),1):
        copia.write(lineas[i])
    
    copia.write(frase)
    
    archivo.close()

    copia = open("copia.txt","r")
    contenido = copia.read()
    print(contenido)
    
# linea_al_final("archivo.txt","el triplehijueputa del menor")

def linea_al_principio(nombre_archivo:str, frase:str):
    
    archivo = open(nombre_archivo,"r")
    copia = open("copia.txt","w")
    lineas = archivo.readlines()

    copia.write(frase + "\n")

    for i in range(0,len(lineas),1):
        copia.write(lineas[i])
        
    archivo.close()

    copia = open("copia.txt","r")
    contenido = copia.read()
    print(contenido)

# linea_al_principio("archivo.txt","el triplehijueputa del menor")

def listar_palabras_de_archivo(nombre_archivo:str) -> list:
    lista_res:list [str] = []    
    palabra_a_agregar:str = ""
    archivo = open(nombre_archivo,"rb")
    contenido = archivo.readlines()
    for i in range(len(contenido)):
        for j in range(len(contenido[i])):
            if (((contenido[i])[j]) == 32 or ((contenido[i])[j]) == 45 or 65 <= ((contenido[i])[j]) <= 90 or 97 <= ((contenido[i])[j]) <= 122 or 48 <= ((contenido[i])[j]) <= 57):
                palabra_a_agregar += chr((contenido[i])[j])
            else:
                if(len([palabra_a_agregar]) >= 5):
                    lista_res += [palabra_a_agregar]
                    palabra_a_agregar = ""
        if palabra_a_agregar != "":
            lista_res += [palabra_a_agregar]
    archivo.close()
    return lista_res
 
# def calcular_promedio_por_estudiante(nombre_archivo_notas:str, nombre_archivo_promedios:str):

# Pilas 

def generar_numeros_al_azar(cantidad:int,desde:int,hasta:int) -> Pila[int]:
    agregados:int = 0
    p = Pila() 
    while(agregados < cantidad):
        n = random.randint(desde,hasta) 
        p.put(n)
        print(n)
        agregados += 1 
    return p    

def cantidad_elementos(p:Pila) -> int:
    contador = 0 
    p2 = Pila()
    while(p.empty() == False):
        contador += 1 
        x = p.get()
        p2.put(x)
    while(p2.empty() == False):
        x = p2.get()
        p.put(x)
    return contador 

def pila_basic() -> Pila[int]:
    p = Pila()
    p.put(10)
    p.put(4)
    p.put(3)
    return p 

def buscar_el_maximo(p:Pila[int]) -> int:
    res:int = 0
    while(cantidad_elementos(p) > 1):
        x = p.get()
        y = p.get()
        if (x >= y):
            p.put(x)
        else:
            p.put(y)
    res = p.get()
    return res 
    
# print(buscar_el_maximo(pila_basic()))

def esta_bien_balanceada(s:str) -> bool:
    
    res:bool = True
    new_list:list[str] = []
    p = Pila()
    contadorpar1 = 0
    contadorpar2 = 0
    for i in range(len(s)):
        new_list += s[i]
    for i in range(len(new_list)):
        p.put(new_list[i])

    while(p.empty()  == False):
        x = p.get()
        if(ord(x) == 40):
            contadorpar1 += 1
        if(ord(x) == 41):
            contadorpar2 += 1
    return contadorpar1 == contadorpar2
    
# Ejercicio 12     

def juntarnumeros(s: str, caracterDistinto: str) -> list[str]:
    caracteres = []
    
    for i in range(len(s)):
        caracteres += s[i]
    palabra:str = ""
    expresion:list [str] = []
    
    for i in range(len(caracteres)):
        if caracteres[i] == caracterDistinto and palabra != "":
            expresion += [palabra]
            palabra = ""
        else:
            palabra += caracteres[i]
    if palabra != "":
        expresion += [palabra]
    return expresion      

def evaluar_expresion(s: str) -> float:
    caracteres = juntarnumeros(s," ")
    p = Pila()
    for caracterActual in caracteres:
        if caracterActual in ["+","-","/","*"]:
            x = float(p.get())
            y = float(p.get())
            if caracterActual == "+":
                res = x + y
                p.put(res)
            if caracterActual == "-":
                res = y - x
                p.put(res)
            if caracterActual == "x":
                res = x*y
                p.put(res)
            if caracterActual == "/":
                res = y/x
                p.put(res)
        else:
            p.put(float(caracterActual))
    x = p.get()
    return x 
