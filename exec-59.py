#Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS.

contador_negativos = 0
contador = 1

while contador <= 10:
    valor = float(input(f"Digite o valor {contador}: "))
    if valor < 0:
        contador_negativos += 1
    contador += 1
print(f"Número de valores negativos: {contador_negativos}")
