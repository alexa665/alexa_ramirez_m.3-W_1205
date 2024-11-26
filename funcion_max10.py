def es_bisiesto(año):
    if (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0):#funcion if, else para sierto o falso 
        return True
    else:
        return False
#ingrese un año
año_usuario = int(input("Ingresa un año para verificar si es bisiesto: "))
#verifica si es bisiesto o no 
if es_bisiesto(año_usuario):
    print(f"El año {año_usuario} es bisiesto.")
else:
    print(f"El año {año_usuario} no es bisiesto.")
