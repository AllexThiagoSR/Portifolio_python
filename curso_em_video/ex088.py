from random import randint
temp = list()
jogos = list()
print('=' * 100)
print(f'{"JOGA NA MEGA SENA":^100}')
print('=' * 100)
while True:
    try:
        quant = int(input('Quantas jogos deseja sortear? ').strip())
        break
    except ValueError:
        print('Digite apenas números.')
print(f'{"=-" * 10}JOGOS{"-=" * 10}')
for i in range(0, quant, 1):
    for j in range(0, 6, 1):
        temp.append(randint(1, 60))
    jogos.append(temp[:])
    temp.clear()
for i in range(0, quant, 1):
    print(f'{i + 1}º jogo: {jogos[i]}')
print(f'{"=-" * 10}BOA SORTE!!!{"-=" * 10}')

