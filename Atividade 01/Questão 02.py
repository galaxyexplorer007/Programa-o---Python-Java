qtd_seg = int(input('Insira a quantidade total de segundos.'))

if qtd_seg < 0:
    print('A quantidade deve ser positiva.')
else:
    dias = qtd_seg // 86400
    resto_dias = qtd_seg % 86400

    horas = resto_dias // 3600
    resto_horas = resto_dias % 3600

    minutos = resto_horas // 60
    segundos = resto_horas % 60

    print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")