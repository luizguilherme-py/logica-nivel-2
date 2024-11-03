#Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um algoritmo que permita a entrada das seguintes informações: a) o número total de mercadorias no estoque; b) o valor de cada mercadoria. Ao final imprimir o valor total em estoque e a média de valor das mercadorias.

num_mercadorias = int(input("Digite o número total de mercadorias no estoque: "))
valor_total = 0
for i in range(1, num_mercadorias + 1):
    valor_mercadoria = float(input(f"Digite o valor da mercadoria {i}: "))
    valor_total += valor_mercadoria
media_valor = valor_total / num_mercadorias
print(f"Valor total em estoque: R$ {valor_total}")
print(f"Média de valor das mercadorias: R$ {media_valor}")
