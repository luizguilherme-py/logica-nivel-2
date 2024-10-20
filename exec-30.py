#Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

if valor1 < valor2 and valor1 < valor3:
  if valor2 < valor3:
    print(f"Ordem crescente: {valor1}, {valor2}, {valor3}")
  else:
    print(f"Ordem crescente: {valor3}, {valor2}, {valor1}")
elif valor2 < valor1 and valor2 < valor3:
  if valor1 < valor3:
    print(f"Ordem crescente: {valor2}, {valor1}, {valor3}")
  else:
    print(f"Ordem crescente: {valor2}, {valor3}, {valor1}")
else:
  if valor1 < valor2:
    print(f"Ordem crescente: {valor3}, {valor1}, {valor2}")
  else:
    print(f"Ordem crescente: {valor3}, {valor2}, {valor1}") 
