numero_impar = int(input("Digite um número ímpar: "))

if numero_impar % 2 != 0:
    numero_anterior = numero_impar - 2
    numero_proximo = numero_impar + 2

    diferenca = (numero_proximo ** 2) - (numero_anterior ** 2)
    print(f"Diferença: {diferenca}")
else:
    print("O número inserido não é ímpar.")