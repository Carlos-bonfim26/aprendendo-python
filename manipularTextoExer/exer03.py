frase = str(input("Digite uma frase: "))

primeira = frase.find("a")
ultima = frase.rfind("a")
frase = frase.lower().count("a");

print("A letra 'a' aparece", frase, "vezes na frase.")
print("Aparecendo a primeira vez na posição:", primeira, "E na última vez na posição:", ultima)