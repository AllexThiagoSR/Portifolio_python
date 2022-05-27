lista = list()
pares = list()
impares = list()
while True:
    while True:
        num = input('Digite um valor: ').strip()
        try:
            num = int(num)
            break
        except ValueError:
            print('Digite apenas números por favor')
    lista.append(num)
    cont = 'a'
    while cont not in 'NnSs':
        cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if cont == 'N':
        break
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print('=' * 100)
print(f'Valores digitados: {lista}')
print(f'Valores pares da lista: {pares}')
print(f'Valores ímpares da lista: {impares}')
