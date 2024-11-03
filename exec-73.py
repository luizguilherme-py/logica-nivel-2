#A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Faça um algoritmos para coletar dados sobre o salário e número de filhos de cada habitante e após as leituras, escrever:

total_salarios = 0
total_filhos = 0
quantidade_habitantes = 0

while True:
    salario = float(input("Digite o salário do habitante (Ou -1 para encerrar): "))
    if salario == -1:
        break
    filhos = int(input("Digite o número de filhos do habitante: "))
    
    total_salarios += salario
    total_filhos += filhos
    quantidade_habitantes += 1
    
media_salarios = total_salarios / quantidade_habitantes if quantidade_habitantes > 0 else 0

print(f"\nTotal de habitantes pesquisados: {quantidade_habitantes}")
print(f"Soma total dos salários: R$ {total_salarios:.2f}")
print(f"Média dos salários: R$ {media_salarios:.2f}")
print(f"Soma total de filhos: {total_filhos}")
