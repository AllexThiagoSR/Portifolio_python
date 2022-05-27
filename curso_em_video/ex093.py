nome = input('Nome do jogador: ').strip().capitalize()
jogador = dict()
gols = list()
while True:
    try:
        partidas = int(input(f'Quantas partidas {nome} jogou? ').strip())
        for i in range(1, partidas + 1, 1):
            gols.append(int(input(f'\tQuantos gols na {i}ª partida? ').strip()))
        break
    except ValueError:
        gols.clear()
        print('Digite apenas números')
jogador['Nome'] = nome
jogador['Partidas jogadas'] = partidas
jogador['Gols em partidas'] = gols[:]
jogador['Gols na temporada'] = sum(gols)
print('=' * 100)
print(jogador)
print('=' * 100)
print(f'{jogador["Nome"]} jogou {jogador["Partidas jogadas"]}:')
for i in jogador['Gols em partidas']:
    print(f'\t-{jogador["Nome"]} fez {i} gol(s) na {jogador["Gols em partidas"].index(i) + 1}ª partida')
print(f'Total de gols na temporada: {jogador["Gols na temporada"]}')
