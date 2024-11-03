#A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Faça um algoritmos para coletar dados sobre o salário e número de filhos de cada habitante e após as leituras, escrever:

total_salarios = 0
total_filhos = 0
quantidade_habitantes = 0
maior_salario = float('-inf')  
pessoas_com_salario_baixo = 0  # 

while True:
    
    salario = float(input("Digite o salário do habitante (salário negativo para encerrar): "))
    

    if salario < 0:
        break


    filhos = int(input("Digite o número de filhos do habitante: "))


    total_salarios += salario
    total_filhos += filhos
    quantidade_habitantes += 1


    if salario > maior_salario:
        maior_salario = salario


    if salario < 150:
        pessoas_com_salario_baixo += 1


media_salarios = total_salarios / quantidade_habitantes if quantidade_habitantes > 0 else 0
media_filhos = total_filhos / quantidade_habitantes if quantidade_habitantes > 0 else 0
percentual_salario_baixo = (pessoas_com_salario_baixo / quantidade_habitantes * 100) if quantidade_habitantes > 0 else 0


print(f"\nMédia de salário da população: R$ {media_salarios:.2f}")
print(f"Média do número de filhos: {media_filhos:.2f}")
print(f"Maior salário dos habitantes: R$ {maior_salario:.2f}")
print(f"Percentual de pessoas com salário menor que R$ 150,00: {percentual_salario_baixo:.2f}%")
