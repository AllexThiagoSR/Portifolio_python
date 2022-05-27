matriz = [[],
          [],
          []]
for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        while True:
            num = input(f'Digite um valor para a posição [{i}, {j}]: ').strip()
            try:
                num = int(num)
                break
            except ValueError:
                try:
                    num = float(num)
                    break
                except ValueError:
                    print('Digite apenas números.')
        matriz[i].append(num)
for i in range(0, len(matriz), 1):
    print()
    for j in range(0, len(matriz[i]), 1):
        print(f'[{matriz[i][j]}]', end=' ')
