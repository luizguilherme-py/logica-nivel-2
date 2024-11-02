#Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero e imprimir o resultado da divisão do primeiro valor lido pelo segundo valor lido. (utilizar a estrutura REPITA).

valor1 = float(input("Digite o primeiro valor: "))
valor2 = 0 

while valor2 == 0:
    valor2 = float(input("Digite o segundo valor (não pode ser zero): "))
    if valor2 == 0:
        print("O segundo valor deve ser diferente de zero. Tente novamente.")

resultado = valor1 / valor2
print(f"O resultado da divisão de {valor1} por {valor2} é: {resultado:.2f}")
