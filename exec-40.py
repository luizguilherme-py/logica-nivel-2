produto = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: "))

total = quantidade * preco_unitario

if quantidade > 100:
    desconto = total * 0.10
elif quantidade >= 50 and quantidade <= 100:
    desconto = total * 0.05
else:
    desconto = 0

total_a_pagar = total - desconto

print(f"Produto: {produto}")
print(f"Total: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
