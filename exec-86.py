# Faça um algoritmo para ler 10 números e armazenar em um vetor. Após isto, o algoritmo deve ordenar os números no vetor em ordem crescente. Escrever o vetor ordenado.

numers = []
for i in range(10):
  num = float(input(f"Digite o {i+1}º número: "))
  numeros.append(num)

numeros.sort()
print("Vetor ordenado em ordem crescente:")
print(numeros)
