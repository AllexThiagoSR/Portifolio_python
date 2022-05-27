from funverinu import is_int
while True:
    while True:
        num = input('Digite um número para ver sua tabuada(números negativos encerram): ').strip()
        if is_int(num):
            num = int(num)
            break
        print('Digite apenas números por favor.')
    if num < 0:
        print('Encerrou')
        break
    print()
    print('TABUADA')
    print('=' * 50)
    for i in range(0, 11, 1):
        print(f'{i:>3} x{num:>3} = {i * num:>3}')
    print()
