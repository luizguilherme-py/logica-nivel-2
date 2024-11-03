#Faça um programa que leia 100 valores e no final, escreva o maior e o menor valor lido.

maior = float('-inf')
menor = float('inf')

for i in range(100):
    valor = float(input(f"Digite o valor {i + 1}: "))

    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f"O maior valor lido foi: {maior}")
print(f"O menor valor lido foi: {menor}")
