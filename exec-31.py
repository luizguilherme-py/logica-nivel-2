#Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam ou não um triângulo. OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lados.

A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do LADO C: "))

if A < B + C and B < A + C and C < A + B:
  print("Os valores formam um triângulo.")
else:
  print(" Os valores não formam um triângulo.")
