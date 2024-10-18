#Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 < valor2:
  print(f"A ordem crescente é: {valor1}, {valor2}")
else:
  print(f"A ordem crescente é: {valor2}, {valor}")
