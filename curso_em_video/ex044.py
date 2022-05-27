from funverinu import is_number
preco_fin = 0.0
print('===== LOJINHO DO SEU ZÉ =====')
preco = input('Qual o preço das compras? R$').strip()
print('=== Formas de pagamento ===')
print('[1] - Dinheiro/cheque à vista\n[2] - À vista no cartão\n[3] - 2x no cartão\n[4] - Mais de 3x no cartão')
forma = input('Qual a opção de pagamento escolhida: ').strip()
if is_number(preco) and is_number(forma):
    preco = float(preco)
    forma = int(forma)
    if forma == 1:
        preco_fin = preco * 0.9
        print('À vista dinheiro/cheque')
        print(f'Preço com 10% de desconto: R${preco_fin:.2f}')
    elif forma == 2:
        preco_fin = preco - (preco * 0.05)
        print('À vista no cartão')
        print(f'Preço com 5% de desconto: R${preco_fin:.2f}')
    elif forma == 3:
        preco_fin = preco
        print('Em até 2x no cartão')
        print(f'Preço formal: R${preco_fin:.2f}, cada parcela ficará R${preco_fin / 2:.2f}')
    elif forma == 4:
        preco_fin = preco * 1.20
        print('Em mais de 3x no cartão')
        vez = int(input('Em quantas vezes foi dividido: ').strip())
        print(f'Preço com 20% de juros: R${preco_fin:.2f}, cada parcela ficará no valor de R${preco_fin / vez:.2f}')
else:
    print('Digite apenas números por favor')
