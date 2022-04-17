a = str(input('Digite uma expressão '))
pilha = list()
for simb in a:
    if simb == '(':
        a.append('(')
    elif simb == ')':
        if len(pilha) > 0:
                pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida')
else:
    print('Sua expressão está errada')

