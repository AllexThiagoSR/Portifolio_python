from random import randint
from funverinu import is_number
from time import sleep
print('=' * 30)
print(f'{"JOGO DE ADIVINHAÇÃO":^30}')
print('=' * 30)
print()
print('Vou pensar em um número entre 0 e 10, tente adivinhar.')
sleep(3)
print('PENSEI')
num_m = randint(0, 10)
num_j = -1
i = 0
while True:  # while not num_j == num_m
    print()
    num_j = input('Qual o seu palpite? ').strip()
    print()
    if is_number(num_j):
        num_j = int(num_j)
        i += 1
        if num_j == num_m:
            print(f'Você acertou, eu realmente pensei em {num_j}')
            break
        elif num_j < num_m:
            print('Um número maior')
        elif num_j > num_m:
            print('Um número menor')
    else:
        print('Digite apenas números por favor.')
        print()
print(f'Você acertou em {i} tentativas.')
