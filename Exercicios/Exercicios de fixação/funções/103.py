def ficha(Nome_do_Jogador='<desconhecido>', gols=0):
    print('=-' * 8)
    ficha = {1: Nome_do_Jogador, 2:gols}
    print(ficha.keys())
    print(ficha.items())
    print(ficha.values())
    print(f'O Jogador {ficha[1]} fez {ficha[2]} gol(s) neste campeonato')


ficha('Airton', 15)
