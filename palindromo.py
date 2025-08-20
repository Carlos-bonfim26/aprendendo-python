text = str(input("Digite um texto: "))

def is_palindrome(string):
    separar = string.split()
    junto = ''.join(separar)
    return junto == junto[::-1]

if is_palindrome(text):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")