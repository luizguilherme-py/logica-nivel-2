#Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável X. Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o vetor M.

A = []

for i in range(10):
    numero = float(input(f"Digite o número {i +1} para o vetor A: "))
    A.append(numero)
    
X = float(input("Digite um número X: "))

M = []

for numero in A:
    M.append(numero * X)
    
print("O vetor M, resultado da multiplicação de A por X, é:")
print(M)
