#Para o enunciado a seguir foi elaborado um algoritmo em Português Estruturado que contém erros, identifique os erros no algoritmo apresentado abaixo: Enunciado: Tendo como dados de entrada o nome, a altura e o sexo (M ou F) de uma pessoa, calcule e mostre seu peso ideal, utilizando as seguintes fórmulas:

nome = input("Digite o nome: ")
sexo = input("Digite o sexo: (M para masculino ou F para feminino:")
altura = float(input("Digite a altura em metros: "))

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = None
    print("Sexo inválido. Diite 'M' para masculino ou 'F' para feminino.")
if peso_ideal is not None:
    print(f"O peso idela para {nome} é: {peso_ideal:.2f} kg")
