#Ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10,20] (inlcuindo os valores 10 e 20 no intervalo) e quantos deles estão fora deste intervalo.

contador_intervalo = 0
contador_fora_intervalo = 0
contador = 1

while contador <= 10:
    valor = float(input(f"Digite o valor {contador}: "))
    if 10 <= valor <= 20:
        contador_intervalo += 1
    else:
        contador_fora_intervalo += 1 
    contador += 1

print(f"Número de valores no intervalo [10, 20]: {contador_intervalo}")
print(f"Número de valores fora do intervalo [10, 20]: {contador_fora_intervalo}")
