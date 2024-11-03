#O mesmo exercício anterior, mas agora não será informado o número de mercadorias em estoque. Então o funcionamento deverá ser da seguinte forma: ler o valor da mercadoria e perguntar ‘MAIS MERCADORIAS (S/N)?’. Ao final, imprimir o valor total em estoque e a média de valor das mercadorias em estoque.

valor_total = 0
contador = 0

while True:
    valor_mercadoria = float(input("Digite o valor da mercadoria: "))
    valor_total += valor_mercadoria
    contador += 1 

    mais_mercadorias = input("MAIS MERCADORIAS (S/N)? ").strip().upper()
    if mais_mercadorias == 'N':
        break

media_valor = valor_total / contador if contador > 0 else 0
print(f"Valor total em estoque: R$ {valor_total:.2f}")
print(f"Média de valor das mercadorias: R$ {media_valor:.2f}")
