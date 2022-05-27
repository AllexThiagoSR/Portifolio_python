from funverinu import is_int
soma = 0
i = 0
while True:
    print('=' * 50)
    while True:
        num = input('Digite um valor inteiro (999 - parar): ').strip()
        if is_int(num):
            num = int(num)
            break
        print('Digite apenas valores inteiros.')
    # if num == 999:
    #     print('Encerra')
    #     break
    # i += 1
    # soma += num
    # OU
    if num != 999:
        i += 1
        soma += num
        continue
    print('ENCERRA')
    break
print(f'Quantidade digitada: {i}')
print(f'Soma: {soma}')
