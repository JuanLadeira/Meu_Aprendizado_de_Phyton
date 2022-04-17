# Criando o desafio de fazer o computador "pensar" em um numero inteiro entre 0 a 5 e peça para o usuario tentar advinhar qual foi o numero
# pelo computador. O programa deverá exibir na tela do usuário se ele venceu ou não.

import random
Numero = int(random.randint(0,5))
print('Tenho um desafio para você...')
print('Você conseguiria advinhar em qual numero de 0 a 5 eu estou pensando?')
n = int(input("Tente advinhar qual numero eu pensei.."))

if Numero == n:
    print('Nossa, como você conseguiu fazer isso? acertou na mosca!')
else:
    print('É,eu sabia que você não era capaz...')