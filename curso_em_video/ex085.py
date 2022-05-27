lista = [[], []]
for i in range(0, 7, 1):
    while True:
        try:
            num = int(input(f'Digite o {i + 1}ª número: ').strip())
            break
        except ValueError:
            print('Digite apenas números.')
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 != 0:
        lista[1].append(num)
print('=' * 100)
print(f'Pares: {sorted(lista[0])}')
print(f'Ímpares: {sorted(lista[1])}')
