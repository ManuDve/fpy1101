renta = int(input("Ingrese su renta anual\n"))

def calcular_impuesto(renta):
    if renta < 550000:
        return 5
    elif renta <= 860000:
        return 15
    elif renta <= 935000:
        return 20
    elif renta <= 1305000:
        return 30
    else:
        return 45

print(f"Su tipo impositivo es {calcular_impuesto(renta)}%")