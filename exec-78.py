#Escreva um algoritmo que permita a leitura dos nomes de 10 pessoas e armaze os nomes lidos em um vetor. Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de pessoa e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

nomes = []

for i in range(10):
    nome = input(f"Digite o nome da pessoa {i + 1}: ")
    nomes.append(nome)
nome_procurado = input("Digite um nome para procurar: ")
if nome_procurado in nomes:
    print("ACHEI!")
else:
    print("NÃO ACHEI!")
