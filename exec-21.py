#A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_por_hora = float(input("Digite o salário por hora: "))

horas_normais_no_mes = 40 * 4
horas_extras = max(0, horas_trabalhadas - horas_normais_no_mes)

valor_horas_extras = horas_extras * salario_por_hora * 1.5 

salario_normal = horas_normais_no_mes * salario_por_hora
salario_total = salario_normal + valor_horas_extras

print(f"O salário total do funcionário é: R$ {salario_total:.2f}")
