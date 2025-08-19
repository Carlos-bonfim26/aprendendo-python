num = str(input("Digite um número entre 0 e 9999:"))

if(len(num)>4 or "-" in num):
    str(input("Digite um número entre 0 e 9999!! burro:"))

tamanho_num = len(num)

dividir_num = list(num)
match(tamanho_num):
    case 4:
        print("Milhares:", dividir_num[0])
        print("centenas:", dividir_num[1])
        print("dezenas:", dividir_num[2])
        print("unidades:", dividir_num[3])
    case 3:
        print("centenas:", dividir_num[0])
        print("dezenas:", dividir_num[1])
        print("unidades:", dividir_num[2])
    case 2:
        print("dezenas:", dividir_num[0])
        print("unidades:", dividir_num[1])
    case 1:
        print("unidades:", dividir_num[0])
