numero = list()

for cont in range(0, 5):
    numero.append(int(input('Digite um numero!!  ')))

print(f'O maior valor digitado foi {max(numero)} nas posições',end = ' ')
for i, v in enumerate(numero):
    if v == max(numero):
        print(f'{(i+1)}...',end = ' ')
print()
print(f'O maior valor digitado foi {min(numero)} nas posições', end = ' ')
for i, v in enumerate(numero):
    if v == min(numero):
        print(f'{(i+1)}...', end = ' ')
print()