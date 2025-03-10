#Faça um algoritmo para ler e armazenar em um vetor a temperatura média de todos os dias do ano. Calcular e escrever: 

#a) Menor temperatura do ano
#b) Maior temperatura do ano
#c) Temperatura média anual
#d) O número de dias no ano em que a temperatura foi inferior a média anual

temperaturas = []

for i in range(365):
  temperatura = float(input(f"Digite a temperatura média do dia {i+1}: "))
  temperaturas.append(temperatura)

menor_temperatura = min(temperaturas)
maior_temperatura = max(temperaturas)
media_anual = sum(temperaturas) / len(temperaturas)

dias_abaixo_media = sum(1 for temp in temperaturas if temp < media_anual)

print(f"\nMenor temperatura do ano: {menor_temperatura}")
print(f"Maiortemperatura do ano: {maior_temperatura}")
print(f"Temperatura média anual: {media_anual:.2f}")
print(f"Número de dias com temperatura abaixo da média anual: {dias_abaixo_media}")
