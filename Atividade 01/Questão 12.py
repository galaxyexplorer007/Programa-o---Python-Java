quantidade_turmas = int(input("Digite a quantidade de turmas: "))
total_alunos = int(input("Digite o número total de alunos: "))

media_alunos = total_alunos / quantidade_turmas

if media_alunos > 40:
    print("Atenção: Alguma turma possui mais de 40 alunos.")
else:
    print(f"Média de alunos por turma: {media_alunos:.2f}")