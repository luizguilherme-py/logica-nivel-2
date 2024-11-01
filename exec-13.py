#Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário escrever NÃO É MAIOR QUE 10!

valor = float(input("Digite um valor: "))
if valor > 10:
  print("É MAIOR QUE 10!")
elif valor == 10:
  print("É exatamente 10!")
else:
  print("NÃO É MAIOR QUE 10!")
