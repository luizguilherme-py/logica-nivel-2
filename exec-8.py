votos_nulos = int(input("Qual o total de votos nulos? "))

votos_validos = int(input("Qual ao total de votos validos? ")) #variaveis 

votos_brancos = int(input("Qual o total de votos brancos? "))

totalDeVotos = votos_nulos + votos_validos + votos_brancos

porcentagemValidos = (votos_validos / totalDeVotos ) * 100
print(porcentagemValidos)

porcentagemNulos = ( votos_nulos / totalDeVotos ) * 100 # calculo
print(porcentagemNulos)

porcentagemBrancos = (votos_brancos / totalDeVotos ) * 100
print(porcentagemBrancos)
