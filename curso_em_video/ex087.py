matriz = [[],
          [],
          []]
soma = soma3 = 0
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
        print(f'[{matriz[i][j]:>3}]', end=' ')
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
        if j == 2:
            soma3 += matriz[i][j]
print()
print('=' * 100)
print(f'Soma de todos os valores pares digitados: {soma}')
print(f'Soma dos valores da terceira coluna: {soma3}')
print(f'O maior valor da segunda linha: {max(matriz[1])}')
