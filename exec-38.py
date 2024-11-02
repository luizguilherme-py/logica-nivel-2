#Uma fruteira está vendendo frutas com a seguinte tabela de preços:

codigo = int(input("Digite o código de usuário: "))

if codigo != 1234:
    print("Usuário inválido!")
else:
    senha = int(input("Digite a senha: "))
    
    if senha != 9999:
        print("Senha incorreta!")
    else:
        print("Acesso permitido")
