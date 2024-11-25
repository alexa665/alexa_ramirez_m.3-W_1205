print(" ")
print("Alexa Guadalupe Ramirez Manzo 1205 3-W")
print(" ")
def max_in_list(lista):#lista 
    if not lista:
        return None  
    max_num = lista[0] #lista vasia
    # segundo elemento
    for num in lista[1:]:
        if num > max_num:
            max_num = num  # ponemos max_num si encontramos un número mayor
    return max_num
numeros = [1, 5, 3, 9, 2]
print(max_in_list(numeros))  #num a imprimir de la lista 
