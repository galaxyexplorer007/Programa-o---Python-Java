usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario != senha:
    print("Login realizado com sucesso.")
else:
    print("Erro: O nome de usuário e a senha não podem ser iguais.")