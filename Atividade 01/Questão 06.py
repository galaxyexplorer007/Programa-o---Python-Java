primos_encontrados = 0
numero_atual = 2
primos = []

while primos_encontrados < 100:
    e_primo = True
    divisor = 2
    
    while divisor <= int(numero_atual ** 0.5):
        if numero_atual % divisor == 0:
            e_primo = False
            break
        divisor += 1

    if e_primo and numero_atual.is_integer():
        primos.append(numero_atual)
        primos_encontrados += 1

    numero_atual += 1

print(primos)