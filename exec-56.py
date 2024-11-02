#Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.

valor = int(input("Digite um valor inteiro entre 1 e 10: "))
while valor < 1 or valor > 10:
    print("Valor inválido! O número deve estar entre 1 e 10.")
    valor = int(input("Digite um valor inteiro entre 1 e 10: "))
print(f"Tabuada de {valor}:")
for i in range(1, 11):
    resultado = valor * i
    print(f"{valor} x {i} = {resultado}")
