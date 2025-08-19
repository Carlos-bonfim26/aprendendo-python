def somaLista(lista):
    acumulador = 0
    for i in lista:
        acumulador += i
    return acumulador

numerosAleatorios = [1, 8, 12, 7]

print(somaLista(numerosAleatorios))
    