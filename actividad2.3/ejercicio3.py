ingredientes_vegetarianos = ["Pimiento", "Cebolla", "Choclo", "Tofu"]
ingredientes = ["Pimiento", "Cebolla", "Choclo", "Tofu", "Pepperoni", "Jamón", "Chorizo", "Salmón"]
es_vegetariana = True
opciones = ["primera", "segunda"]
ingredientes_maximos = 1
def validar_opcion(opcion):
    opcion = opcion.lower()
    if opcion=="si" or opcion=="s" or opcion=="sí":
        return True
    elif opcion=="no" or opcion=="n":
        return False
    else:
        opcion = input("Respuesta inválida, ingrese sí o no\n")
        return validar_opcion(opcion)


def mostrar_ingredientes():
    ingrediente = 0
    print(f"Ingrese su {opciones[ingredientes_maximos]}] opción")
    if validar_opcion(eleccion):
        for x in range(len(ingredientes_vegetarianos)):
            print(f"{x+1}. {ingredientes_vegetarianos[x]}") 
        ingrediente = int(input())      
    else:
        for x in range(len(ingredientes)):
            print(f"{x+1}. {ingredientes[x]}")
        ingrediente = int(input())
        if ingrediente > 3:
            es_vegetariana = False   
    ingredientes_maximos = ingredientes_maximos - 1
    return eleccion

eleccion = input("¡Quiere una pizza vegetariana? Si o No\n")
eleccion_1 = mostrar_ingredientes()
eleccion_2 = mostrar_ingredientes()
print("Es vegetariana") if es_vegetariana else print("No es vegetariana")






