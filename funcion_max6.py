print>(" ")
print("alexa guadalupe ramirez manzo 3-w 1205")
print(" ")
# Ingresar el año en curso
año_actual = int(input("Ingresa el año en curso: "))
# Inicializamos una lista para almacenar los datos de las personas
personas = []
# Ingresar datos de tres personas
for i in range(3):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    año_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
    edad = año_actual - año_nacimiento
    personas.append((nombre, año_nacimiento, edad))
# Imprimir los resultados
print("\nEdad de las personas en el año", año_actual)
for persona in personas:
    nombre, año_nacimiento, edad = persona
    print(f"{nombre} nació en {año_nacimiento} y cumplirá {edad} años en el año {año_actual}.")

