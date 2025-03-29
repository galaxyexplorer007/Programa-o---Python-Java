p1 = 1
p2 = 2
p3 = 2

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

media_ponderada = ((n1 * p1) + (n2 * p2) + (n3 * p3))/(p1 + p2 + p3)

print('A média ponderada é igual a: ', media_ponderada)