#lista de nombres a utilizar
nombres = ["Maria", "Alexa", "Valeria", "Laura", "Tagle", "Valentin", "Piedra", "Paola", "Jose", "Leonardo"]
#ingrese la letra con la que quiere buscar
letra = input("Ingresa la letra con la que quieres verificar los nombres: ").lower()
#cuantos nombres comiensan con esa letra
contador = sum(1 for nombre in nombres if nombre.lower().startswith(letra))
#impresion de resultado
print(f"\nCantidad de nombres que comienzan con la letra '{letra.upper()}': {contador}")
