salario_inicial = float(input("Digite o salário inicial: "))
anos = int(input("Digite o número de anos: "))

salario_atual = salario_inicial
percentual_aumento = 1  # Percentual inicial é 100%

for ano in range(anos):
    salario_atual += salario_atual * (percentual_aumento / 100)
    percentual_aumento *= 2  # O percentual dobra a cada ano

print(f"Salário atual após {anos} anos: R${salario_atual:.2f}")