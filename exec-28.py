#Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

if valor1 > valor2 and valor1 > valor3:

    if valor2 > valor3:
        soma = valor1 + valor2
    else:
        soma = valor1 + valor3
elif valor2 > valor1 and valor2 > valor3:
  
    if valor1 > valor3:
        soma = valor2 + valor1
    else:
        soma = valor2 + valor3
else:

    if valor1 > valor2:
        soma = valor3 + valor1
    else:
        soma = valor3 + valor2

print(f"A soma dos dois maiores valores é: {soma:.2f}")
