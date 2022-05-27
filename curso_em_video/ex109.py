import moeda
while True:
    try:
        preco = float(input('Digite um preço? R$ ').strip())
        break
    except ValueError:
        print('Apenas valores numéricos')
print(f'O dobro do preço {moeda.formatar(preco)} é {moeda.dobro(preco, formata=True)}')
print(f'A metade do preço {moeda.formatar(preco)} é {moeda.metade(preco, formata=True)}')
print(f'O preço {moeda.formatar(preco)} mais 50% é {moeda.aumentar(preco, 50, formata=True)}')
print(f'O preço {moeda.formatar(preco)} menos 70% {moeda.diminuir(preco, 70, formata=True)}')

