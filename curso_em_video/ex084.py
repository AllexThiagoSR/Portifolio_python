pessos = list()
mais = menos = 0
pessoa = list()
while True:
    pessoa.append(input('Nome: ').strip().capitalize())
    while True:
        try:
            pessoa.append(float(input('Peso: ').strip()))
            break
        except ValueError:
            print('Digite apenas números')
    pessos.append(pessoa[:])
    pessoa.clear()
    print('Pessoa cadastrada')
    print('=' * 100)
    cont = 'a'
    while cont not in 'NnSs':
        cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
    print('=' * 100)
    if cont == 'N':
        print('Encerra')
        break
for i in range(0, len(pessos), 1):
    if i == 0 or mais < pessos[i][1]:
        mais = pessos[i][1]
    if i == 0 or menos > pessos[i][1]:
        menos = pessos[i][1]
print(f'O maior peso cadastrado foi {mais:.2f} kg de: ', end='')
for i in pessos:
    if i[1] == mais:
        print(f'[{i[0]}]', end=' ')
print()
print(f'O menor peso casdastrado foi {menos:.2f} kg de ', end='')
for i in pessos:
    if i[1] == menos:
        print(f'[{i[0]}]', end=' ')
print()
print(f'Quantidade de pessoas cadastradas: {len(pessos)}')
