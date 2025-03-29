valor_total = int(input('Insira o valor total das mercadorias: '))
taxa = (valor_total/100) * 50

if valor_total <= 500:
    print('Não há imposto sobre esse valor.')
else:
    valor_final = valor_total + taxa
    print(f'O valor inserido recebeu uma taxa de 50%, assim o valor final é: R${valor_final}')