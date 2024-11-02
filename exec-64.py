#Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior a 40 devem ser somados. Escreva o valor final da soma efetuada.

soma_menor_40 = 0

for i in range(1, 11):
    numero = float(input(f"Digite o número {i}: "))
    if numero < 40:
        soma_menor_40 += numero
        
print(f"A soma dos números menores que 40 é: {soma_menor_40}")
