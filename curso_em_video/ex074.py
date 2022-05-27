from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Valores sorteados:')
for i in tupla:
    print(i)
print()
print(f'Maior valor: {max(tupla)}')
print(f'Menor valor: {min(tupla)}')
