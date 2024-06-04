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

# Colas 

from queue import Queue as Cola

def generar_num_al_azar(cantidad:int,desde:int,hasta:int) -> Cola[int]:   
    c = Cola()
    for i in range(0,cantidad,1):
        x = random.randint(desde,hasta)
        c.put(x)
    return c 

# Ejercicio 14

def cantidad_de_elem(c:Cola) -> int:
    res = 0
    c2 = Cola()
    while(c.empty() == False):
        res += 1 
        x = c.get()
        c2.put(x)
    while(c2.empty() == False): 
        x = c2.get()
        c.put(x)
    return res 

def cola_trivial() -> Cola:
    c = Cola()
    c.put(1)
    c.put(91)
    c.put(92)
    c.put(2)
    c.put(4)
    c.put(5)
    c.put(6)
    c.put(61)
    c.put(8)
    c.put(9)
    c.put(30)
    c.put(11)
    c.put(12)
    return c 

# Ejercicio 15 

def buscar_maximo(c:Cola[int]) -> int:
    res = 0 
    while(cantidad_de_elem(c) > 1):
        x = c.get()
        y = c.get()
        if x > y:
            c.put(x)
        else:
            c.put(y)
    res = c.get()
    return res 
    
# Ejercicio 16

def armar_secuencia_de_bingo() -> Cola:
    num = 100
    s:list[int] = []
    for i in range(num):
        s += [i] 
    t:list[int] = []
    for j in range(num):
        x = random.choice(s)
        t += [x]
        s.remove(x)
    c = Cola()
    for r in range(num):
        c.put(t[r])
    return c 

def pertenece(x:int,lista:list[int]) -> bool:
    res:bool = False
    for i in range(len(lista)):
        if lista[i] == x:
            res = True 
    return res  

def jugar_carton_de_bingo(carton : list[int]) -> int:
    jugadas = 0
    ganadas = 0
    objetivo = len(carton)
    bolillero = armar_secuencia_de_bingo()
    while(ganadas != objetivo):
            x = bolillero.get()
            jugadas += 1  
            if pertenece(x,carton): 
                ganadas += 1
    return jugadas 
     
# Ejercicio 17 

def n_pacientes_urgentes(c : Cola[(int, str, str)]) -> int:
    urgentes:int = 0
    c2 = Cola()
    while(c.empty() == False):
        x = c.get()
        c2.put(x)
        if x[0] == 1 or x[0] == 2 or x[0] == 3:
            urgentes += 1 
    while(c2.empty() == False):
        y = c2.get()
        c.put(y)
    return urgentes 
        
def cola_comp() -> Cola[(int, str, str)]:
    c = Cola()
    c.put((10,"A","oculista"))
    c.put((10,"B","medico"))
    c.put((10,"C","medico"))
    c.put((10,"D","medico"))
    return c 

# Ejercicio 18 

def atencion_a_clientes(clientes: Cola[(str, int, bool, bool)]) -> Cola[(str, int, bool, bool)]:
    clientes_copy = clonar_cola(clientes)
    c_res = Pila()
    for i in range(cantidad_de_elem(clientes_copy)):
        x = clientes_copy.get()
        if x[3] == True:
            c_res.put(x)
        else:
            clientes_copy.put(x)
    for i in range(cantidad_de_elem(clientes_copy)):
        x = clientes_copy.get()
        if x[2] == True:
            c_res.put(x)
        else:
            clientes_copy.put(x)
    for i in range(cantidad_de_elem(clientes_copy)):
        x = clientes_copy.get()
        c_res.put(x)
    return c_res

def clonar_cola(c: Cola[(str, int, bool, bool)]) -> Cola[(str, int, bool, bool)]:
    copia = Cola()
    lista_clientes:list [(str, int, bool, bool)] = []
    for i in range(cantidad_de_elem(c)):
        x = c.get()
        copia.put(x)
        lista_clientes += [x] 
    for i in range(len(lista_clientes)):
        c.put(lista_clientes[i])
    return copia

def cola_comp2() -> Cola[(int, str, str)]:
    c = Cola()
    c.put(("a",1,True,False))
    c.put(("b",2,False,False))
    c.put(("c",3,False,True))
    c.put(("d",4,True,True))
    return c 
