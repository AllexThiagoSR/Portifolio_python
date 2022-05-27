from itertools import count
from funverinu import is_int
soma = 0
med = 0.0
j = 0
mai = int()
men = int()
for i in count(start=1):
    print('=' * 50)
    while True:
        num = input('Digite um número inteiro: ').strip()
        if not is_int(num):
            print()
            print('Digite apenas números inteiros.')
            continue
        num = int(num)
        break
    if i == 1 or num > mai:
        mai = num
    if i == 1 or num < men:
        men = num
    soma += num
    cont = 'o'
    while cont not in 'SsNn':
        cont = input('Digitar mais um número? [s/n]').strip().upper()[0]
    if cont in 'Nn':
        print('Encerra')
        j = i
        break
    print('Continua')
    print()
med = soma / j
print(f'Média: {med:.2f}')
print(f'Maior: {mai}')
print(f'Menor: {men}')
