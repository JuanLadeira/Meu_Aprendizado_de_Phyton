n = int(input('Digite o numero da tabuada que deseja.'))

for c in range(0,11):
    t = n * c
    print('{} * {} = {}'.format(n,c,t))

