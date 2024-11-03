#Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada. Escrever a média da turma e o resultado da contagem.

notas = []

for i in range(20):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)
media = sum(notas) / len(notas)

contagem_acima_media = sum(1 for nota in notas if nota > media)

print(f"A média da turma é: {media:.2f}")
print(f"Número de alunos com nota acima da média: {contagem_acima_media}")
