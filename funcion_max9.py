print(" ")
print("alexa guadalupe ramirez manzo 3-w 1205")
print(" ")
def contar_vocales(palabra):
    #palabrs a minusculas 
    palabra = palabra.lower()
    #diccionario para almacenamiento
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    #bucle para buscar cada letra
    for letra in palabra:
        if letra in vocales:
            vocales[letra] += 1
    #impresion de resultados
    print("Conteo de vocales:")
    for vocal, cantidad in vocales.items():
        print(f"{vocal.upper()}: {cantidad}")
#ingrese una palabra
palabra_usuario = input("Ingresa una palabra para contar las vocales: ")
contar_vocales(palabra_usuario)
