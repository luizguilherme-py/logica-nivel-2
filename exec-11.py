#Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):

temperatura_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

temperatura_celsius = (5 / 9) * (temperatura_fahrenheit - 32)

print("A temperatura correspondente em graus Celsius é: {:.2f}".format(temperatura_celsius))
