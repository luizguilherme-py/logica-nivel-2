#Faça um algoritmo para ler o código e o preço de 15 produtos, calcular e escrever: - o maior preço lido - a média aritmética dos preços dos produtos

soma_precos = 0
maior_preco = float('-inf')

for i in range(15):
    codigo = input(f"Digite o código do produto {i + 1}: ")
    preco = float(input(f"Digite o preço do produto {i + 1}: "))

    soma_precos += preco

    if preco > maior_preco:
        maior_preco = preco

media_precos = soma_precos / 15

print(f"O maior preço lido foi: {maior_preco}")
print(f"A média dos preços dos produtos é: {media_precos:.2f}")
