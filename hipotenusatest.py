import math

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))

cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

def calcular_hipotenusa(oposto, adjacente):
    return math.hypot(oposto, adjacente)

print(f"A hipotenusa é: {calcular_hipotenusa(cateto_oposto, cateto_adjacente):.2f}")