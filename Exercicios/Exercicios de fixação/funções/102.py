def fatorial(num = 1,  show=False):
    """
    A  formula faz a operação matematica fatorial do numero informado.
    :type show: Se for 'True' mostrará os resultados dos calculos.
    :param show: pré setado como falso para não mostrar os calculos dos valores.
    :param num: Informar o Valor da fatorial desejada.
    :return: retorna  o resultado da operação fatorial do numero informado.
    """
    f = 1
    for c in range(num,0,-1):
        if show is True:
            f *= c
            if c == 1:
                break
            else:
                if num == c:
                    print(f'O fatorial do numero {num} é:')

                print(f'{f} * {c-1} = {f*(c-1)}', end='\n\n')
        else:
            f *= c
            if c == 1:
                print(f' {c} ', end='')
            else:
                print(f' {c} *', end='')
    if show is True:
        print(f'Resultado = {f}',  end=' ')
        print('')
        print("-="*10)
    else:
        print(f' = {f}', end=' ')
    return f

#programa principal

fatorial(5,True)