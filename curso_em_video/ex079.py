valores = []
while True:
    while True:
        num = input('Digite um valor: ').strip()
        try:
            num = int(num)
            if num not in valores:
                print(f'Valor cadastrado')
                valores.append(num)
                break
            else:
                print('Valor já cadastrado digite outro por favor')
        except ValueError:
            print('Digite apenas números')
    cont = 'a'
    print('=' * 100)
    while cont not in 'NnSs':
        cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if cont == 'N':
        print('Encerra')
        break
print('=' * 100)
for i in sorted(valores):
    print(i)
