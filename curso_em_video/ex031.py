km = input('Digite a distância da viagem em km: ').strip()
preco = 0
if km.isnumeric():
    km = float(km)
    if km <= 200:
        preco = km * 0.5
    elif km > 200:
        preco = km * 0.45
    print(f'Para uma viagem de {km} km, o preço da passagem será R${preco:.2f}')
else:
    print('Digite apenas números por favor')
