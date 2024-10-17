#Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores

total_eleitores = int(input("Digite o número total de eleitores: "))
votos_brancos = int(input("Digite o número de votos brancos: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))

# Passo 2: Calcular os percentuais
percentual_brancos = (votos_brancos / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_validos = (votos_validos / total_eleitores) * 100

# Passo 3: Exibir os percentuais
print("Percentual de votos brancos: {:.2f}%".format(percentual_brancos))
print("Percentual de votos nulos: {:.2f}%".format(percentual_nulos))
print("Percentual de votos válidos: {:.2f}%".format(percentual_validos))
