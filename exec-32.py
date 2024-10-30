#Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")

gols_time1 = int(input(f"Digite o número de gols marcados pelo {time1}: "))
gols_time2 = int(input(f"Digite o número de gols marcados pelo {time2}: "))

if gols_time1 > gols_time2:
  print(f"O vencedor é: {time1}")
elif gols_time2 > gols_time1:
  print(f"O vencedor é: {time2}")
else:
  print("EMPATE")
