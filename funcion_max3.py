print(" ")
print("Alexa Guadalupe Ramirez Manzo 3-W 1205")
print(" ")
def filtrar_palabras(lista_palabras, n):  #lista para las palabras y n para el número de palabras
    return [palabra for palabra in lista_palabras if len(palabra) > n]

palabras = ["como", "soldado", "nala", "alexa", "lesly"] #impresion para las palabras
resultado = filtrar_palabras(palabras, 4)
print(resultado)
