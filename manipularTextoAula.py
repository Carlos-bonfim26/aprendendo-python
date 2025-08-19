frase = "Hoje tem Tricolor"

#fatiamento
print(frase[9:17]) # tricolor
print(frase[2:17:2])# j e rclr
print(frase[:5]) # Hoje
print(frase[5:]) # tem Tricolor
print(frase[5::3]) # t il

#contagem e fatiamento 
print(frase.count("o", 0, 8)) #1

# analisar string
print(len(frase)) # 17
print(frase.count("o")) # 3
print(frase.find("tem")) # 5
print(frase.find("a")) # -1, não encontrado
print("Hoje" in frase) # True

# transformar
print(frase.replace("Tricolor", "São Paulo"))
print(frase.lower()) # hoje tem tricolor
print(frase.upper()) # HOJE TEM TRICOLOR

print(frase.capitalize()) # Hoje tem tricolor
frase2 = "Estou aprendendo o python"

print(frase2.title()) # Estou Aprendendo O Python

frase3 = "   Olá, Mundo!   "

print(frase3.strip()) # Olá, Mundo!
print(frase3.rstrip()) #    Olá, Mundo!

#divisão
print(frase.split()) # ['Hoje', 'tem', 'Tricolor']

frase_split = frase.split()

print("-".join(frase_split)) # Hoje-tem-Tricolor