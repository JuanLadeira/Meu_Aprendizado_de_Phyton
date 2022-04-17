valores = list()
while True:
    v = (int(input('Digite um valor  ')))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso')
    elif v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso')
    else:
        print('Esse valor já foi cadastrado, por favor, digite um valor diferente!')
        v = (int(input('Digite um valor  ')))
        if v not in valores:
            valores.append(v)
            print('Valor adicionado com sucesso')
        else:
            print('Ei amigão, se liga!! digou numero repetido de Exercicios de fixação')
    d = str(input('Deseja continuar? [S/N] ').upper())
    if d != "S" and d != "N":
        print('Digite [S] para SIM ou [N] para não')
    elif d == 'N':
        break
    print('-='*30)
valores.sort()
print(f'Você digitou os valores {valores}', end = "")
print()
