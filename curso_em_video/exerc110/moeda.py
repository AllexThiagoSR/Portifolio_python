def formatar(valor):
    valor = f'R$ {valor:.2f}'
    return valor.replace('.', ',')


def aumentar(valor, porce=0, formata=False):
    resu = valor + ((valor * porce) / 100)
    return formatar(resu) if formata else resu


def diminuir(valor, porce=0, formata=False):
    resu = valor - ((valor * porce) / 100)
    return formatar(resu) if formata else resu


def dobro(valor, formata=False):
    return valor * 2 if formata is False else formatar(valor * 2)


def metade(valor, formata=False):
    return valor / 2 if formata is not True else formatar(valor / 2)


def resumo(valor, aument=0, redu=0, formata=False):
    valor_2 = formatar(valor) if formata else f'R$ {valor:.2f}'
    print('=' * 81)
    print(f'{"RESUMO DO VALOR":^81}')
    print('=' * 81)
    print(f'Valor analizado: {valor_2}')
    print(f'Dobro do preço: {dobro(valor=valor, formata=formata)}')
    print(f'Metade do preço: {metade(valor=valor, formata=formata)}')
    print(f'{aument}% de aumento: {aumentar(valor=valor, porce=aument, formata=formata)}')
    print(f'{redu}% de redução: {diminuir(valor=valor, porce=redu, formata=formata)}')
    print('_' * 81)
