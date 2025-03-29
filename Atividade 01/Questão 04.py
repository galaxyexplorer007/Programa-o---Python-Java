try:
    dias = int(input('Por quantos dias ele alugou o carro?: '))
    km = int(input('Quantos quilômetros ele rodou?: '))

    if dias < 0 or km < 0:
        print('Não tem como ser negativo.')
    elif km <= 100:
        valor_total = dias * 90
        print(f'O valor total a ser pago é de: R${valor_total}')
    elif km > 100:
        custo_excedente = (km - 100) * 12
        valor_total = (dias * 90) + custo_excedente
        print(f'O valor total a ser pago é de: R${valor_total}')
    else:
        pass
except ValueError:
    print('Só pode inserir números inteiros.')