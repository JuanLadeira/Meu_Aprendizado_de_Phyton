n1 = int(input('Digite um numero '))
n2 = int(input('Digite mais um numero '))
n3 = int(input('só mais um! '))

if n1 > n2 and n1 > n3:
    print('O numero {} é o maior número entre os informados'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O numero {} é o maior número entre os informados'.format(n2))
elif n3 > n2 and n3 > n1:
    print('O numero {} é o maior número entre os informados'.format(n3))
elif n1 == n2  and n1 > n3:
    print('Os numeros {} e {} são iguais e maiores que {}'.format(n1,n2,n3))
elif n1 == n3 and n1 > n2:
    print('Os numeros {} e {} são iguais e maiores que {}'.format(n1,n3,n2))
elif n2 == n3 and n2 > n1:
    print('Os numeros {} e {} são iguais e maiores que {}'.format(n2,n3,n1))
else:
    print('Os números são iguais')
