#Faça um algoritmo para ler uma quantidade e a seguir ler esta quantidade de números. Depois de ler todos os números, o algoritmo deve apresentar na tela o maior dos números lidos e a média dos números lidos.

quantidade = int(input("Digite a quantidade de números: "))

soma = 0
maior = float('-inf')

for i in range(quantidade):
    numero = float(input(f"Digite o número {i + 1}: "))
    
    soma += numero
    
    if numero > maior:
        maior = numero
        
media = soma / quantidade if quantidade > 0 else 0

print(f"O maior número lido foi: {maior}")
print(f"A média dos números lidos é: {media:.2f}")
