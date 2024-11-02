#Escreva um algoritmo para ler as notas da 1a. e 2a. avaliações de um aluno, calcule e imprima a média (simples) desse aluno. Só devem ser aceitos valores válidos durante a leitura (0 a 10) para cada nota.

nota1 = -1
nota2 = -1

while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Digite a primeira nota (de 0 a 10): "))
    if nota1 < 0 or nota1 > 10:
        print("Nota inválida! A nota deve estar entre 0 e 10.")

while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Digite a segunda nota (de 0 a 10): "))
    if nota2 < 0 or nota2 > 10:
        print("Nota inválida! A nota deve estar entre 0 e 10.")

media = (nota1 + nota2) / 2

print(f"A média do aluno é: {media:.2f}")
