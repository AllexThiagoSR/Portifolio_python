def area(largura, comprimento):
    return largura * comprimento


print(f'{"Controle de Terrenos":^30}')
print('=' * 30)
while True:
    try:
        larg = float(input('LARGURA (m): ').strip())
        compr = float(input('COMPRIMENTO (m): ').strip())
        break
    except ValueError:
        print('Digite apenas valores numéricos')
print('=' * 100)
print(f'Área do terreno: {area(largura=larg, comprimento=compr):.2f} m²')
