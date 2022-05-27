def fatorial(valor, show=False):
    resu = 1
    mostra = ''
    for i in range(valor, 0, -1):
        resu *= i
        mostra += f' {i} *'
    if show:
        mostra = mostra[1:-1]
        mostra += f'= {resu}'
        return resu, mostra
    else:
        return resu


print(fatorial(valor=12, show=True))
