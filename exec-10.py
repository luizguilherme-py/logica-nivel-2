#Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa de R$ 700,00 para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor. 

numero_carros_vendidos = int(input("Digite o número de carros vendidos: "))
valor_total_vendas = float(input("Digite o valor total das vendas: "))
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
comissao_por_carro = 700.00  
percentual_comissao = 0.05    


comissao_fixa_total = numero_carros_vendidos * comissao_por_carro
comissao_percentual_total = valor_total_vendas * percentual_comissao


salario_final = salario_fixo + comissao_fixa_total + comissao_percentual_total


print("O salário final do vendedor é: {:.2f}".format(salario_final))
