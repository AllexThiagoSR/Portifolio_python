lis = list()
while True:
    while True:
        num = input('Digite um valor: ').strip()
        try:
            num = int(num)
            break
        except ValueError:
            try:
                num = float(num)
                break
            except ValueError:
                print('Digite apenas números por favor')
    lis.append(num)
    cont = 'a'
    while cont not in 'NnSs':
        cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if cont == 'N':
        break
print('=' * 100)
print(f'A quantidade de valores digitados foi: {len(lis)}')
print(f'Lista ordenada decrescentemente: {sorted(lis, reverse=True)}')
tem = 'Há o valor 5 nessa lista' if 5 in lis else 'Não há o valor 5 nessa lista'
print(f'{tem}')
