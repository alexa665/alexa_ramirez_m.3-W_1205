print(" ")
print("alexa guadalupe ramirez manzo 3-w 1205")
print(" ")
edades = [] #lista para organizar
#bucle for para ingresar las edades de las diez personas 
for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    edades.append(edad)
#tupla para organizar la informacion
edades_tupla = tuple(edades)
#encontrar cuantas personas tienen mas de 20 años
contador_mayores_20 = sum(1 for edad in edades_tupla if edad > 20)
#Impresion de resultado
print(f"\nCantidad de personas con edades superiores a 20: {contador_mayores_20}")
