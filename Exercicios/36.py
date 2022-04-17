#escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai pérguntar o valor da casa,
# o o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou
#então o empréstimo será negado

preço = int(input('Qual é o valor da casa que você pretende comprar?'))
salario = int(input('Qual é o valor do seu salário?'))
tempo = int(input('Pretende pagar a casa em quantos anos?'))
meses = tempo * 12
regra = salario * 0.3
prestação = preço / meses

if prestação > regra:
    print('Infelizmente temos que informar que seu salário não é compatível para concedermos o emprestímo no valor desejado')
    print('Portanto, não temos escolha a não ser negar o empréstimo.')
else:
    print('Ficamos muito felizes em informar que seu perfil é compátivel com o valor do empréstimo.')
    print('A prestação será no valor de {:.2f} que será paga em {} meses'.format(prestação,meses))
