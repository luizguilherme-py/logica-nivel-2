#Ler o número de alunos existentes em uma turma e, após isto, ler as notas destes alunos, calcular e escrever a média aritmética dessas notas lidas.

num_alunos = int(input("Digite o número de alunos na turma: "))

soma_notas = 0

for i in range(1, num_alunos + 1): 
    nota = float(input(f"Digite a nota do aluno {i}: "))  
    soma_notas += nota

media = soma_notas / num_alunos

print(f"A média aritmética das notas é: {media}")
