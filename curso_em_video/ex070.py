cesta = dict({'Produtos': [], 'Preços': [], 'Quantidade': []})
total = 0
barato = [0, '']
ac = 0
print('=' * (len('  Lojinho do Seu Zé') + 2))
print('  Lojinho do Seu Zé')
print('=' * (len('  Lojinho do Seu Zé') + 2))
while True:
    produto = input('Digite o nome do produto: ').strip().capitalize()
    while True:
        preco = input('Digite o preço desse produto: R$ ').strip()
        quanti = input('Quantos desse produto: ').strip()
        try:
            preco = float(preco)
            quanti = int(quanti)
            break
        except ValueError:
            print('Digite apenas números.')
            print()
    cesta['Produtos'].append(produto)
    cesta['Preços'].append(preco)
    cesta['Quantidade'].append(quanti)
    print('Produto adicionado à cesta')
    print('=' * 100)
    cont = 'p'
    while cont not in 'NnSs':
        cont = input('Deseja adicionar mais produtos? (S/N)').strip().upper()[0]
    if cont in 'Nn':
        print('Encerra...')
        break
    print('=' * 100)
print('=' * 100)
for i in range(0, len(cesta['Produtos']), 1):
    if i == 0 or cesta['Preços'][i] < barato[0]:
        barato[0] = cesta['Preços'][i]
        barato[1] = cesta['Produtos'][i]
    if cesta['Preços'][i] > 1000:
        ac += 1
    total += (cesta['Preços'][i] * cesta['Quantidade'][i])
    print(f'Produto: {cesta["Produtos"][i]}')
    print(f'Preço: R${cesta["Preços"][i]:.2f}')
    print(f'Quantidade: {cesta["Quantidade"][i]}')
print('=' * 100)
print(f'Preço total da compra: R${total:.2f}')
print(f'Produto mais barato: {barato[1]}')
print(f'Preço: R${barato[0]:.2f}')
print(f'Temos {ac} produtos que custam mais que R$ 1000,00')
