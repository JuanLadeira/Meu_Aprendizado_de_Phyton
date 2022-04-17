#Desenvolva um programa que pergunte a distância de uma uiagem em km.
#Calcule o preço da passagem cobrando 0,50 por km até 200 km e 0,45 para mais longas.

distancia = int(input('Por favor, Informe a distância da viagem em km  '))
preço1 = distancia * 0.50
preço2 = distancia * 0.45
if distancia <= 200:
    print('O preço da sua passagem será de {} reais'.format(preço1))
else:
    print('O preço da sua passagem será de {} reais'.format(preço2))

print('Desejamos uma boa viagem.')