#O mesmo exercício anterior, mas agora, considere que o segundo valor lido poderá ser maior ou menor que o primeiro valor lido, ou seja, deve-se testá-los.

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

soma_intervalo = 0

if valor1 > valor2:
    valor1, valor2 = valor2, valor1  


for i in range(valor1, valor2 + 1):  
    soma_intervalo += i

print(f"A soma dos inteiros entre {valor1} e {valor2} é: {soma_intervalo}")
