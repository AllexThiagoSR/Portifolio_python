import moeda
while True:
    try:
        preco = float(input('Digite um preço? R$ ').strip())
        break
    except ValueError:
        print('Apenas valores numéricos')
print(f'O dobro do preço {moeda.formatar(preco)} é {moeda.formatar(moeda.dobro(preco))}')
print(f'A metade do preço {moeda.formatar(preco)} é {moeda.formatar(moeda.metade(preco))}')
print(f'O preço {moeda.formatar(preco)} mais 50% é {moeda.formatar(moeda.aumentar(preco, 50))}')
print(f'O preço {moeda.formatar(preco)} menos 70% {moeda.formatar(moeda.diminuir(preco, 70))}')
