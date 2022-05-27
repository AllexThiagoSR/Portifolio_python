from funverinu import is_int
iu = 0
soma = 0
while True:
    while True:
        num = input('Digite um número inteiro(999 - para o programa): ').strip()
        print()
        if is_int(num):
            num = int(num)
            break
        print('Apenas números inteiros por favor.')
        print()
    # As três formas entregam o mesmo resultado
    # if num != 999:
    #     soma += num
    #     iu += 1
    #     continue
    # break
    # OU
    # if num != 999:
    #     soma += num
    #     iu += 1
    # elif num == 999:
    #     break
    # OU
    if num == 999:
        break
    soma += num
    iu += 1
print(f'Quantidade de números digitados: {iu}')
print(f'Soma dos números digitados: {soma}')
