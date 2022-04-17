lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
     lista.append(n)
     print('Valor Adicionado com Sucesso')
    else:
        print('O valor já foi digitado por favor, digite um valor diferente.')
        n = int(input('Digite um valor: '))
        if n not in lista:
            lista.append(n)
            print('Valor Adicionado com Sucesso')
            pos = 0
            while pos < len(lista):
                if n <= lista[pos]:
                    lista.insert(pos, n)
                    print(f'O valor {n} foi adicionado na posição {pos}')
                    break
        else:
            break
    d = str(input('Deseja continuar? [S/N] ').upper())
    if d != "S" and d != "N":
        print('Digite [S] para SIM ou [N] para não')
    elif d == 'N':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 apareceu {lista.count(5)} vezes nas posições {lista.index(5)}')
else:
    print(f'O valor 5 não foi encontrado na lista')
