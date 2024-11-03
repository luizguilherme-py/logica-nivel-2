#O mesmo exercício anterior, mas agora deve escrever o menor elemento do vetor e a respectiva posição dele nesse vetor.

Q = []

for i in range(20):
    while True:
        valor = float(input(f"Digite um número positivo para a posição {i + 1}: "))
        if valor > 0:
            Q.append(valor)
            break
        else:
            print("Poe favor, digite apenas números positivos.")
maior_valor = Q[0]
menor_valor = Q[0]
posicao_maior = 0
posicao_menor = 0

for i in range(1, len(Q)):
    if Q[i] > maior_valor:
        maior_valor = Q[i]
        posicao_maior = i
    if Q[i] < menor_valor:
        menor_valor = Q[i]
        posicao_menor = i
        
print(f"O maior elemento de Q é: {maior_valor} e ocupa a posição {posicao_maior + 1} no vetor.")
print(f"O menor elemento de Q é: {menor_valor} e ocupa a posição {posicao_menor + 1} no vetor.")
