from math import ceil, floor, trunc,sqrt
print('Faça um programa que leia o comprimento do cateto oposto  e do catedo adjacente de um triangulo  retangulo e  calcule e mostre o comprimento da hipotenusa')
co = int(input('Digite o valor do cateto oposto'))
ca = int(input('Digite o valor do cateto adjacente'))

h = sqrt((co**2 + ca**2))

print('O valor do comprimento da hipotenusa equivale a {}'.format(h))
