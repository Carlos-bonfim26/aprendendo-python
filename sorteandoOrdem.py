import random

def sorteia_ordem(array):
    random.shuffle(array)
    return array

array_numeros = [1, 2, 3, 4, 5, 7, 6]

print("Ordem original:", array_numeros)
print("Ordem aleatória:", sorteia_ordem(array_numeros))