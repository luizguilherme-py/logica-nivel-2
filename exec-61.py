#Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.

soma = 0 
contador = 1

while contador <= 10:
    valor = float(input(f"Digite o valor {contador}: "))
    soma += valor
    contador += 1

media = soma / 10

print(f"A média aritmética dos valores é: {media}")
