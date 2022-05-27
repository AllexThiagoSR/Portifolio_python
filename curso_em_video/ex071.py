print('=' * 49)
print(f'{"BANQUINHO":^49}')
print('=' * 49)
ced = 50
cedu = 0
while True:
    valor = input('Digite o valor que deseja sacar: R$ ').strip()
    try:
        valor = float(valor)
        break
    except ValueError:
        print('Digite apenas números.')
tot = valor
print('=' * 100)
while True:
    if tot >= ced:
        cedu = tot // ced
        tot = tot % ced
    else:
        if cedu > 0:
            print(f'Total de {cedu:.0f} cédulas de R$ {ced},00')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cedu = 0
        if tot == 0:
            break
print(f'Total sacado: R$ {valor:.2f}')
print('=' * 100)
print('Tchau. Volte sempre.')
