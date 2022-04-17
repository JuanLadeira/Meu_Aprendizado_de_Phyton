pessoas = {}
equipe = []
for c in range(0,3):
    pessoas['nome'] = str(input('Digite o nome'))
    pessoas['idade'] = int(input('Digita a idade'))
    pessoas['sexo'] = str(input('Digite o sexo (M/F/NA)'))
    equipe.append(pessoas.copy())

for n in equipe:
    for k, v in n.items():
        print(f'O campo {k} tem valor {v}.')