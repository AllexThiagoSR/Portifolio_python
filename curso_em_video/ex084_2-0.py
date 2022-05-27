pessoas = list()
mais = menos = 0
while True:
    pessoas.append(input('Nome: ').strip().capitalize())
    while True:
        try:
            pessoas.append(float(input('Peso: ').strip()))
            break
        except ValueError:
            print('Digite apenas números.')
    print('Pessoa cadastrada')
    print('=' * 100)
    cont = 'a'
    while cont not in 'NnSs':
        cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
    print('=' * 100)
    if cont == 'N':
        print('Encerra')
        break
mais = max(pessoas[1::2])
menos = min(pessoas[1::2])
print('=' * 100)
print(f'O maior peso cadastrado foi {mais:.2f} kg de ', end='')
for i in range(0, len(pessoas), 1):
    if pessoas[i] == mais:
        print(f'[{pessoas[i - 1]}]')
print()
print(f'O menor peso cadastrado foi {menos:.2f} kg de', end='')
for i in range(0, len(pessoas), 1):
    if pessoas[i] == menos:
        print(f'[{pessoas[i - 1]}]')
