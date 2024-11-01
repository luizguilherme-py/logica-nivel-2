#Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e a soma das idades do homem mais novo com a mulher mais velha.

h1, h2 = int(input("Idade do primeiro homem: ")), int(input("Idade do segundo homem: "))
m1, m2 = int(input("Idade da primeira mulher: ")), int(input("Idade da primeira mulher: "))

homem_mais_velho, homem_mais_novo = max(h1, h2), min(h1, h2)
mulher_mais_velha, mulher_mais_nova = max(m1, m2), min(m1, m2)

print("Soma do homem mais velho com a mulher mais nova:", homem_mais_velho + mulher_mais_nova)
print("Soma do homem mais novo com a mulher mais velha:", homem_mais_novo = mulher_mais_velha)
