#Ler 2 valores, calcular e escrever a soma dos inteiros existentes entre os 2 valores lidos (incluindo os valores lidos na soma). Considere que o segundo valor lido será sempre maior que o primeiro valor lido.

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor (maior que o primeiro): "))

soma_intervalo = 0

for i in range(valor1, valor2 + 1):  
    soma_intervalo += i

print(f"A soma dos inteiros entre {valor1} e {valor2} é: {soma_intervalo}")
