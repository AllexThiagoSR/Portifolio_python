from funverinu import is_number
while True:
    fat = 1
    while True:
        num = input('Digite um valor par ver seu fatorial: ').strip()
        if is_number(num):
            num = int(num)
            break
        else:
            print('Digite apenas números por favor.')
            continue
    print(f'{num}! =', end=' ')
    for i in range(1, num + 1, 1):
        print(f'{i}', end=' ')
        print(f' x ' if i < num else f' = ', end=' ')
        fat *= i
    print(f'{fat}')
    cont = 'a'
    while cont not in 'NnSs':
        cont = input('Quer ver mais um fatorial? [s/n] ').strip().upper()[0]
        if cont not in 'NnSs':
            print('Resposta inválida')
        print()
    if cont == 'N':
        print('Encerra')
        break
    elif cont == 'S':
        print('Continua')
