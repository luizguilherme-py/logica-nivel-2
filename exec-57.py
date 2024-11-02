#Reescreva o exercício 50 utilizando a estrutura REPITA e um CONTADOR.

valor = int(input("Digite um valor inteiro entre 1 e 10: "))
while valor < 1 or valor > 10:  
    print("Valor inválido! O número deve estar entre 1 e 10.")
    valor = int(input("Digite um valor inteiro entre 1 e 10: "))

contador = 1

print(f"Tabuada de {valor}:")
while contador <= 10: 
    resultado = valor * contador
    print(f"{valor} x {contador} = {resultado}")  
    contador += 1 
