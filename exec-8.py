#Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário

salario_atual = float(input("Digite o salário mensal atual do funcionário: "))
percentual_reajuste = float(input("Digite o percentual de reajuste: "))

novo_salario = salario_atual + (salario_atual * percentual_reajuste / 100)

print("O novo salário do funcionário é: {:.2f}".format(novo_salario))
