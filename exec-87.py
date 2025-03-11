#O mesmo exercício anterior, mas depois de ordenar os elementos do vetor em ordem crescente, deve ser lido mais um número qualquer e inserir esse novo número na posição correta, ou seja, mantendo a ordem crescente do vetor.

def remover_numero(vetor, numero):
  if numero in vetor:
    vetor.remove(numero)
    return vetor
  else:
    print(f"O número {numero} não existe no vetor.")
    return vetor
vetor = []
print("Digite 20 números para o vetor:")
for i in range(20):
  num = int(input(f"Digite o número que deseja verificar: "))
vetor_resultante = remover_numero(vetor, numero)
print("Vetor resultante:", vetor_resultante)
