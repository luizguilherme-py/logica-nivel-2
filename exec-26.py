#Ler um valor e escrever se é positivo, negativo ou zero.

valor = float(input("Digite um valor: "))
if valor > 0:
  print("O valor é positivo.")
elif valor < 0:
  print("O valor é negativo.")
else:
  print("O valor é zero.")
