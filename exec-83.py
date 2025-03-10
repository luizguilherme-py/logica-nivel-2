#Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa

numeros = []

for i in range(20):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

print("Os números na ordem inversa são:")
for numero in reversed(numeros):
    print(numero)
