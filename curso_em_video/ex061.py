from funverinu import is_number


def converte(val):
    try:
        val = int(val)
    except ValueError:
        val = float(val)
    return val


print('GERADOR DE PA')
print('=' * 50)
while True:
    while True:
        termo_1 = input('Primeiro termo: ').strip()
        razao = input('Razão: ').strip()
        if is_number(termo_1) and is_number(razao):
            termo_1 = converte(termo_1)
            razao = converte(razao)
            break
        else:
            print('Digite apenas números por favor.')
            continue
    i = 0
    while i < 10:
        print(termo_1, end=' -> ')
        termo_1 += razao
        i += 1
    print('FIM')
    cont = 'a'
    while cont not in 'NsSn':
        cont = input('Mais uma PA? ').strip().upper()[0]
    print('=' * 50)
    if cont in 'Ss':
        print('Continua')
        continue
    print('Encerrou')
    break
