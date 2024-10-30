#Ler dois valores e imprimir uma das três mensagens a seguir:
#‘Números iguais’, caso os números sejam iguais 
#‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
#‘Segundo maior’, caso o segundo seja maior que o primeiro.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 == valor2:
  print("Números iguais")
elif valor1 > valor2:
  print("O primeiro é maior")
else:
  print("O segundo é maior")
