numero = (int(input('Digite um numero ')),
          int(input('Digite outro numero ')),
          int(input('Digite mais um numero ')),
          int(input('Digite o ultimo numero ')),)
print(f'Você digitou os valores {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1}ª posição')
else:
    print('O valor 3 não apareceu nenhuma vez')
print('os valores pares digitados foram',end='')
for n in numero:
    if n % 2 == 0
        print(n, end='')