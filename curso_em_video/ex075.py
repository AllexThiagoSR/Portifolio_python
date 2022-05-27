from random import randint
tupla = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))
ap_9 = 0
print('Valores sorteados:')
for i in tupla:
    print(i)
    if i == 9:
        ap_9 += 1
print()
print('Valores pares:')
for valor in tupla:
    print(valor) if valor % 2 == 0 else ...
print()
print(f'O valor 9 apareceu {ap_9} vezes')
try:
    print(f'O valor 3 apareceu na posição {tupla.index(3)}')
except ValueError:
    print('Não há o valor 3 nessa tupla')
