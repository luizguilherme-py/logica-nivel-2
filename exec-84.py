#Faça um algoritmo para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma dos elementos do vetor A com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.

N = int(input("Digite o valor de N (tamanho dos vetores): "))

A = []
B = []
Soma = []

print("Digite os elementos do vetor A:")
for i in range(N):
    valor = int(input(f"A[{i+1}]: "))
    A.append(valor)

print("Digite os elementos do vetor B:")
for i in range(N):
    valor = int(input(f"B[{i+1}]: "))
    B.append(valor)

for i in range(N):
    Soma.append(A[i] + B[i])

print("O vetor Soma é:")
print(Soma)
