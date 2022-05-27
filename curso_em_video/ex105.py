def notas(*args, sit=False):
    retor = {'Quantidade': len(args), 'Maior': max(args), 'Menor': min(args), 'Média': sum(args) / len(args)}
    if sit:
        if retor['Média'] >= 7:
            retor['Situação'] = 'Boa'
        elif retor['Média'] >= 5:
            retor['Situação'] = 'Razoavel'
        else:
            retor['Situação'] = 'Ruim'
    return retor


print(notas())
