from funverinu import is_number
from copy import deepcopy


def pagamentos(forma='pix'):
    if forma == 'pix' or forma == '1':
        return 'pix'
    elif forma == 'vista' or forma == '2':
        return 'à vista'
    elif forma == 'credito' or forma == '3':
        return 'cartão de crédito'
    else:
        return 'não há essa opção'


def somar(som):
    so = 0
    for s in som:
        so = so + s
    return so


def produtos(lis):
    print('Lista de Produtos: ')
    for h in range(0, len(lis)):
        for c, va in lis[h].items():
            lin(f'  Preço da camiseta: R${va[0]:.2f}, Preço que foi comprada: R${va[1]:.2f}')
            print(f'  Tipo de camiseta: {c}, Código do produto: {h}')
            print(f'  Preço da camiseta: R${va[0]:.2f}, Preço que foi comprada: R${va[1]:.2f}')


def lin(fra):
    print('=' * (len(fra) + 4))

# Esse dicionário contém os produtos
camisas = [{'Camiseta_Gola_Polo': [79.90, 70]},
           {'Camiseta_regata': [34.90, 30]},
           {'Camiseta_Social': [144.90, 130]},
           {'Camiseta_feminina': [69.90, 60]},
           {'Camiseta_Gola_V': [49.90, 40]},
           {'Camiseta_Gola_U': [39.90, 30]}]
o = 1
vendas = []
vend = dict()
val = []
lucro = []
prods = []
formas_pagamen = {'pix': [0], 'à vista': [0], 'cartão de crédito': [0]}
while True:
    produtos(camisas)
    print()

    while True:
        p = input('Digite o código do produto comprado(Apenas aperte enter se não tiver mais nenhum produto): ').strip()
        print()
        if is_number(p):
            p = int(p)

            if p >= len(camisas):
                print(f'Produto não cadastrado, só há produtos dos códigos 0 até {len(camisas) - 1}')
                continue

            print(f'{o}º item comprado:')
            for k, v in camisas[p].items():
                print(f'Produto: {k}\nPreço: R${v[0]:.2f}')
                quant = int(input('Foram compradas quantas unidades desse produto? ').strip())
                prods.append(k)
                val.append(v[0] * quant)
                lucro.append(v[0] * quant - v[1] * quant)
                print()

        elif p == '':
            break
        else:
            print('Digite apenas números por favor')
            print()
            continue
        o += 1

    while True:
        print('Digite 1 ou pix - para pix\nDigite 2 ou vista - para à vista\nDigite 3 ou credito - para cartão de crédito')
        baguio = input('Digite a opção de pagamento: ').strip().lower()
        baguio = pagamentos(forma=baguio)
        if not baguio == 'não há essa opção':
            formas_pagamen[baguio].append(sum(val))
            break
        else:
            print(baguio)
    # Finalizou a compra
    o = 1
    vend['Produtos_da_venda'] = prods[:]
    vend['Preço_total_da venda'] = somar(val)
    vend['Lucro_da_venda'] = somar(lucro)
    vendas.append(deepcopy(vend))
    prods.clear()
    val.clear()
    lucro.clear()
    print(f'Vendas até o momento: {vendas}')
    print()
    cont = input('(Enter para registrar outra venda) (Exit para encerrar o dia)...').strip().upper()
    if cont == 'EXIT':
        break

o = 0
t = 0
print()
vendas = (r for r in vendas)

for i in vendas:
    o += i['Preço_total_da venda']
    t += i['Lucro_da_venda']
print(f'Valor total das vendas do dia: R${o:.2f}')
print(f'Lucro total do dia: R${t:.2f}')

for k, v in formas_pagamen.items():
    print(f'Vendas {k}: R${sum(v):.2f}')
