from random import randint
from time import sleep
from operator import itemgetter
dados = dict()
while True:
    try:
        quantidade_jogadores = int(input('Quantos jogadores são? ').strip())
        break
    except ValueError:
        print('Digite apenas números.')
print('=' * 100)
for i in range(1, quantidade_jogadores + 1, 1):
    dado = randint(1, 6)
    print(f'O jogador {i} tirou: {dado}')
    dados[f'Jogador {i}'] = dado
    sleep(0.5)
print('=' * 100)
j = 1
print('  == RANKING DE JOGADORES ==')
for i in sorted(dados.items(), key=itemgetter(1), reverse=True):
    print(f'{j:>4}º Lugar: {i[0]}, com {i[1]}')
    sleep(1)
    j += 1
