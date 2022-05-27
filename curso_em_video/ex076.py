lista_produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso',
                  9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('=' * 51)
print(f'{"Produtos":^51}')
print('=' * 51)
for i in range(0, len(lista_produtos), 1):
    if i % 2 == 0:
        print(f'{lista_produtos[i]:.<40}', end='')
        continue
    print(f'R${lista_produtos[i]:>7.2f}')
print('=' * 51)
