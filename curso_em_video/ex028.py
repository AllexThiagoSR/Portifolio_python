from random import randint
from time import sleep
a = 'Vou pensar em um número entre 0 e 10, tente adivinhar'
print('\033[1;34m=' * (len(a) + 4))
print('  Vou pensar em um número entre 0 e 10, tente adivinhar')
print('=' * (len(a) + 4))
while True:
    nu = ''
    print('\033[m')
    pensei = randint(0, 10)
    print('PENSEI!!!')
    while not nu.isnumeric():
        nu = input('Em que número acha que eu pensei? ').strip()
        if not nu.isnumeric():
            print('isso não é número, tente de novo')
    if nu.isnumeric():
        nu = int(nu)
    print('Perai', end='')
    for i in range(0, 3, 1):
        sleep(0.5)
        print('.', end='')
    print()
    if nu == pensei:
        print(f'\033[1;32mPARABÉNS!!! Eu realmente pensei em {nu}')
    else:
        print(f'\033[1;31mHihi trouxa, eu pensei em {pensei}, não em {nu}')
    print('\033[m')
    de = input('Quer jogar novamente? ').strip().upper()[0]
    if de == 'N':
        print('Beleza, bye')
        break

