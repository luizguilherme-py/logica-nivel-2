#Acrescente uma mensagem 'NOVO CÁLCULO (S/N)?' ao final do exercício [48]. Se for respondido 'S' deve retornar e executar um novo cálculo, caso contrário deverá encerrar o algoritmo.

def calcular_media():
    nota1 = -1   
    nota2 = -1  

    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Digite a primeira nota (de 0 a 10): "))
        if nota1 < 0 or nota1 > 10:
            print("Nota inválida! A nota deve estar entre 0 e 10.")

    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Digite a segunda nota (de 0 a 10): "))
        if nota2 < 0 or nota2 > 10:
            print("Nota inválida! A nota deve estar entre 0 e 10.")

    media = (nota1 + nota2) / 2

    print(f"A média do aluno é: {media:.2f}")

while True:
    calcular_media() 

    novo_calculo = input("NOVO CÁLCULO (S/N)? ").strip().upper()
    
    if novo_calculo != 'S':
        print("Encerrando o programa.")
        break  
