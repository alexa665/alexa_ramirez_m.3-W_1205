print(" ")
print("Alexa GUadalupe Ramirez Manzo 3-W 1205")
print(" ")
def mas_larga(lista_de_palabras): #lista para palabra mas larga 
    return max(lista_de_palabras, key=len)

palabras = ["hola", "adios", "babay", "hello"] #lista de palabras
resultado = mas_larga(palabras)
print(resultado)  
