#Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor.

Q = []

for i in range(20):
    while True:
        valor = float(input(f"Digite um número positivo para a posição {i + 1}: "))
        if valor > 0:
            Q.append(valor)
            break  
        else:
            print("Por favor, digite apenas números positivos.")

maior_valor = Q[0]
posicao_maior = 0

for i in range(1, len(Q)):
    if Q[i] > maior_valor:
        maior_valor = Q[i]
        posicao_maior = i

print(f"O maior elemento de Q é: {maior_valor} e ocupa a posição {posicao_maior + 1} no vetor.")
