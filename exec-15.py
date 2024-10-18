#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

num_macas = int(input("Digite o número de maçãs compradas: "))

if num_macas >= 12:
  preco = 1.00
else:
  preco = 1.30

custo_total = num_macas * preco

print(f"O custo total da compra é R$ {custo_total:.2f}")
