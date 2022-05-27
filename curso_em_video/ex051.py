from funverinu import is_number
print('=' * (len('10 TERMOS DE UM PA') + 4))
print('  10 TERMOS DE UM PA')
print('=' * (len('10 TERMOS DE UM PA') + 4))
term1 = input('Digite o primeiro termo: ').strip()
raz = input('Digite a razão: ').strip()
if is_number(term1) and is_number(raz):
    term1 = int(term1)
    raz = int(raz)
    print(term1, end=' -> ')
    for i in range(0, 9, 1):
        term1 += raz
        print(term1, end=' -> ')
print('Fim meu fi')
