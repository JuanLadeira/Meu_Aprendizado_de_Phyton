#Faça um programa que leia a idade de um jóvem e diga se já passou o tempo para que ele se aliste
#Se já esta na hora de se alistar ou se ainda falta tempo para se alistar
from math import fabs
nascimento = int(input('Olá, jovem, por favor, me informe seu ano de nascimento  '))
limite = 18
idade = 2022 - nascimento
l2 = fabs(idade - limite)
if idade > nascimento:
    print('Você já deveria ter se alistado há {} anos, meu jovem'.format(l2))
elif idade == nascimento:
    print('Esse é o momento de se alistar, corra meu jovem')
else:
   if l2 > 1:
       print('Se acalme jovem, ainda não faltam {} anos para que chegue o momento!'.format(l2))
   else:
       print('Se acalme meu jovem ainda falta {} ano para que chegue o momento!'.format(l2))



