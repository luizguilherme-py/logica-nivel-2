
preco_alcool = 2.90
preco_gasolina = 3.30

litros = float(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").upper()

if tipo_combustivel == 'A':
    
    if litros <= 20:
        desconto = 0.03  
    else:
        desconto = 0.05  
    preco_total = litros * preco_alcool * (1 - desconto)

elif tipo_combustivel == 'G':
    
    if litros <= 20:
        desconto = 0.04  
    else:
        desconto = 0.06  
    preco_total = litros * preco_gasolina * (1 - desconto)

else:
    print("Tipo de combustível inválido.")
    preco_total = 0  


if preco_total > 0:
    print(f"Valor a ser pago: R$ {preco_total:.2f}")
