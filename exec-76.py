#Imagine que exista um comando chamado "posiciona (x,y)" em alguma linguagem de programação. Onde o X representaria a coluna que algo deve ser impresso na tela, e Y a linha que algo deve ser impresso na tela. Desta forma, o algoritmo abaixo:

#início
#posiciona (10,2)
#escrever ‘Olá’
#fim

#Escreveria a palavra ‘Olá’ na segunda linha da tela, a partir da 10 coluna. Baseado nesta situação, escreva um algoritmo, utilizando este comando 'posiciona' citado, que desenhe na tela um retângulo de 60 colunas (a partir da coluna 1 da tela) e 10 linhas (a partir da linha 1 da tela), sendo que a borda deste retângulo será formada pelo caractere ‘+’. Lembre que somente a primeira e última linha deverão ter todas as colunas preenchidas com o caractere ‘+’. As demais linhas (entre 2 e 9) só terão as colunas 1 e 60 preenchidas. A aparência deste retângulo deve ser parecida com a figura abaixo:


largura = 60
altura = 10

for linha in range(1, altura + 1):
    if linha == 1 or linha == altura:
        
        print('+' * largura)
    else:
        print('+' + ' ' * (largura - 2) + '+')
