# Una empresa que tiene salas de juegos para todas las edades quiere calcular de forma automática el precio
# que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad
# y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis,
# si tiene entre 4 y 18 años debe pagar 3500 y si es mayor de 18 años, 5000.
# Crear un programa en el cual el sistema pregunta por la cantidad de usuarios que ingresaran
# dependiendo su edad y mostrar cuanto le saldrá a la familia la entrada a los juegos.



precios = {
    "ticket_niño": 0,
    "ticket_adolescente": 3500,
    "ticket_adulto": 5000
}

def consultar_edad():
    edad = int(input("Ingrese su edad\n"))
    return edad

def consultar_cantidad_tickets():
    cantidad_tickets = int(input("Ingrese la cantidad de tickets\n"))
    return cantidad_tickets

def calcular_total(edad, cantidad_tickets, total):
    if edad<4:
        total = total + (precios["ticket_niño"] * cantidad_tickets)
        return total
    elif edad<19:
        total = total + (precios["ticket_adolescente"] * cantidad_tickets)
        return total
    else:
        total = total + (precios["ticket_adulto"] * cantidad_tickets)
        return total

def iniciar_programa():
    total = 0
    cantidad = consultar_cantidad_tickets()
    edad = consultar_edad()
    print(f"El total es: ${calcular_total(edad, cantidad, total)}")

iniciar_programa()