n = int(input('Digite um numero para saber se ele é um numero primo ou não '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
    else:
        print('\033[30m', end='')
    print('{} '.format(c), end='')



# duas condições: divisivel por si mesmo = 1 e divisivel por 1 igual a si mesmo