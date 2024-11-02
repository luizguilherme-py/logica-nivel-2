#Modifique o exercício anterior para aceitar somente valores maiores que 0 para N. Caso o valor informado (para N) não seja maior que 0, deverá ser lido um novo valor para N.

N = int(input("Digite um valor inteiro maior que ZERO: "))
while N <= 0: 
    print("Valor inválido! O número deve ser maior que ZERO.")
    N = int(input("Digite um valor inteiro maior que ZERO: "))
for numero in range(1, N + 1):
    print(numero)
