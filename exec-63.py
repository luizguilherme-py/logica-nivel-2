#Escreva um algoritmo para ler 10 números e ao final da leitura escrever a soma total dos 10 números lidos.

soma_total = 0 

for i in range(1, 11):
    numero = float(input(f"Digite o número {i}: "))
    soma_total += numero
    
print(f"A soma total dos 10 números é: {soma_total}")
