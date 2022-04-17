#Equação do segundo grau
import math
from time import sleep
a = int(input('Digite o valor de a '))
b = int(input('Digite o valor de b '))
c = int(input('Digite o valor de c '))

equação = '{}²+{}+{} = 0'.format(a, b, c)
delta = (b ** 2) + (-4 *(a * c))
print('calculando...')
sleep(3)
print('Delta = b^2 - 4 * a * c')
print('Portanto...')
print('Delta = ({})^2 - 4 * ({}) * ({}).'.format(b, a, c))
print('Portanto, o Valor de delta é igual {}'.format(delta))

if delta < 0:
    print('O Delta é {}, um numero negativo, logo, não existe solução.'.format(delta))
    breakpoint()
raizdelta = math.sqrt(delta)

x1 = (-b + raizdelta) / 2 * a
x2 = (-b - raizdelta) / 2 * a

print('Na equação é {}, o valor de delta é igual a {}'.format(equação, delta))
print('Aguarde um momento, estou calculando as raizes')
sleep(2) and print('...')
print('A primeira raiz é igual a {} e a segunda raiz é igual a {}'.format(x1, x2))
