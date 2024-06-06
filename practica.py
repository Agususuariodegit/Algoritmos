def cantidad_de_apariciones(c:list[int]) -> list[tuple]:
    
    tuplas:list[tuple] = []
    
    caracteres_dist = []
    for i in range(len(c)):
        if not c[i] in caracteres_dist:
            caracteres_dist.append(c[i])

    for i in range(len(caracteres_dist)):
        lista:list = []
        for j in range(len(c)):
            if caracteres_dist[i] == c[j]:
                lista.append(c[j])
        tuplas.append((caracteres_dist[i],len(lista)))

    return tuplas        
                

def separar_palabras(contenido:str,caracteresDistintos:list[str]) -> list[list[str]]:
    resultado: list[list[str]] = []
    expresion :list[str] = []
    palabra = "" 
    # while len(expresion) < 5:
    #     for i in range(len(contenido)):
    #             if contenido[i] in caracteresDistintos:
    #                 expresion.append(palabra)
    #                 palabra = ""
    #             else:
    #                 palabra += contenido[i]
    # if palabra != "":
    #     expresion.append(palabra)
    # resultado.append(expresion)
    # return resultado

    for i in range(len(contenido)):
        if len(expresion) < 4:
            caracterActual = contenido[i]
            if caracterActual in caracteresDistintos:
                expresion.append(palabra)
                palabra = ""
            else:
                palabra += caracterActual
        else:
            caracterActual = contenido[i]
            resultado.append(expresion)
            expresion = []
        
    if palabra != "":
        expresion.append(palabra)
    if expresion != []:
        resultado.append(expresion)
    return resultado

print(separar_palabras("hola,como,estas,mucho,gusto,todo,bien,menor",[","]))


      
