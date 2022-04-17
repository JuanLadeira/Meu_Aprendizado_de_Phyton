#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80 km/h mostre uma mensagem dizendo que ele recebeu uma multa
#A multa vai custar 7 reais por cada km acima do limite.

carro = int(input('Qual foi a velocidade do carro?'))
multa = (carro - 80) * 7
if carro > 80:
    print('Informamos que o senhor recebeu uma multa no valor de {}'.format(multa))
else:
    print('Tudo segue dentro dos conformes.')
