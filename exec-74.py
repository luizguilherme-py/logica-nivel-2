#Escreva um algoritmo que imprima a tabuada (de 1 a 10) para os números de 1 a 10.

for i in range(1, 11):
    print(f"Tabuada do {i}:")
    
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")

print()
