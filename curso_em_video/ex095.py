jogadores = list()
gols = list()
while True:
    nome = input('Nome do jogador: ').strip().capitalize()
    while True:
        try:
            partidas = int(input(f'Quantas partidas {nome} jogou? ').strip())
            for i in range(1, partidas + 1, 1):
                gols.append(int(input(f'\tQuantos gols na {i}ª partida? ').strip()))
            break
        except ValueError:
            gols.clear()
            print('Digite apenas números')
    jogadores.append({'Nome': nome, 'Partidas jogadas': partidas, 'Gols em partidas': gols[:], 'Gols na temporada': sum(gols)})
    gols.clear()
    cont = 'a'
    while cont not in 'NnSs':
        cont = input('Deseja continuar? (S/N) ').strip().upper()[0]
    print('=' * 100)
    if cont == 'N':
        break

while True:
    print(f'{"No.":}| {"Nome":<15}')
    for i in jogadores:
        print(f'{jogadores.index(i):>3}| {i["Nome"]:<15}')
    print('=' * 100)
    while True:
        try:
            desen = int(input('Deseja ver o desempenho de qual jogador? (999 - parar) ').strip())
            break
        except ValueError:
            print('Digite apenas valores numéricos')
    if desen == 999:
        break
    k = jogadores[desen]
    print('=' * 100)
    print(f'{k["Nome"]} jogou {k["Partidas jogadas"]} partidas:')
    for i in k['Gols em partidas']:
        print(f'\t-{k["Nome"]} fez {i} gol(s) na {k["Gols em partidas"].index(i) + 1}ª partida')
    print(f'Total de gols na temporada: {k["Gols na temporada"]}')
    print('=' * 100)
