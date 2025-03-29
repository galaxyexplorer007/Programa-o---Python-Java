numero = int(input("Digite um número inteiro maior que 1: "))

if numero > 1:
    eh_primo = True
    divisor = 2

    while divisor <= int(numero ** 0.5):
        if numero % divisor == 0:
            eh_primo = False
            break
        divisor += 1

    if eh_primo:
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")
else:
    print("Número deve ser maior que 1.")