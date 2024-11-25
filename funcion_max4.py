print(" ")
print("Alexa Guadalupe Ramirez Manzo 3-W 1205")
print(" ")
cadena = input("Por favor, ingresa una cadena: ")#ingrese una cadena 
#letras mayusculas contador
contador_mayusculas = 0
for caracter in cadena:    #bucle for para recorrer la cadena
    if caracter.isupper():
        contador_mayusculas += 1

print(f"La cadena tiene {contador_mayusculas} letras mayúsculas.") #imprime el conteo de letras mayusculas
