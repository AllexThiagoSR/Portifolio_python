def leiadinheiro(frase=''):
    while True:
        dinheiro = input(frase).strip()
        dinheiro = dinheiro.replace(',', '.') if ',' in dinheiro else dinheiro
        try:
            dinheiro = float(dinheiro)
            break
        except ValueError:
            print(f'ERRO: "{dinheiro}" é um preço inválido.')
    return dinheiro
