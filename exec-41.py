#Faça um algoritmo para ler as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula abaixo e escrever o conceito do aluno de acordo com a tabela de conceitos mais abaixo:

#Média_de_aproveitamento = N1 + N2 * 2 + N3 * 3 7 

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media_ex = float(input("Média dos Exercícios: "))

media_aprov = (n1 + n2 * 2 + n3 * 3 + media_ex) / 7

if media_aprov >= 9.0:
    conceito = "A"
elif  media_aprov >= 7.5:
    conceito = "B"
elif media_aprov >= 6.0:
    conceito = "C"
else:
    conceito = "D"
    
print(f"Média de Aproveitamento: {media_aprov:.2f}")
print(f"Conceito: {conceito}")
