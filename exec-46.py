#Acrescentar uma mensagem de 'VALOR INVÁLIDO' no exercício [44] caso o segundo valor informado seja ZERO.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor (não pode ser zero): "))

while valor2 == 0:
    print("Valor inválido! O segundo valor deve ser diferente de zero.")
    valor2 = float(input("Digite o segundo valor (não pode ser zero): "))

resultado = valor1 / valor2
print(f"O resultado da divisão de {valor1} por {valor2} é: {resultado:.2f}")
