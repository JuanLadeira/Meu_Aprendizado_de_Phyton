lista = list()

for c in range(0,5):
    n = int(input('Digite um numero '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'O Valor {n} Adicionado na posição {c+1}')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'O valor {n} foi adicionado na posição {pos}')
                break
            pos +=1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
