#É possivel formar um tringulo?
r1 = int(input('Digite o valor da primeira reta'))
r2 = int(input('Digite o valor da segunda reta'))
r3 = int(input('Digite o valor da terceira reta'))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possivel formar um triangulo, as retas cumprem com o pré requisito.')
else:
    print('Não é possivel formar um triangulo com as retas informadas')



