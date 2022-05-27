from exerc110.moeda import resumo  # ou from moeda import resumo
while True:
    try:
        preco = float(input('Digite um preço? R$ ').strip())
        break
    except ValueError:
        print('Apenas valores numéricos')
resumo(valor=preco, aument=20, formata=True, redu=12)
