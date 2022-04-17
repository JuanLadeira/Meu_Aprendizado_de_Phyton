nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()

cores ={'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\03[7;30m'}

m1 = 'Encaminhe o paciente para a sala AMARELA'
m2 = 'Encaminhe o paciente para a sala BRANCA'
m3 = 'Responda a suspeita de doença infetocontagiosa com SIM OU NAO'

# PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_infectocontagiosa=="SIM":
    print('{}{}{}'.format(cores['amarelo'], m1, cores['amarelo']))
elif doenca_infectocontagiosa=="NAO":
    print('{}{}{}'.format(cores['pretoebranco'], m2, cores['azul']))
else:
    print('{}{}{}'.format(cores['azul'], m3, cores['azul']))


# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero=input("Digite o gênero do paciente: ").upper()
    if genero=="FEMININO" and idade>10:
        gravidez=input("A paciente está grávida? ").upper()
        if gravidez=="SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")