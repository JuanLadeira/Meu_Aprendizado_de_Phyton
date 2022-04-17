#Escreve um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
#Para salários superiores a 1200 reais, calcule um aumento de 10%
#para iguais ou inferiores um aumento de 15%
salario = int(input('Digite o valor do seu salário'))
c1 = salario * 1.15
c2 = salario * 1.10

if salario <= 1200:
    print('O seu salário recebeu um aumento de 15% e a partir de hoje será {} reais!!'.format(c1))
else:
    print('O seu salário recebeu um aumento de 10% e a partir de hoje será {} reais!!'.format(c2))
