try:
    aluno = dict()
    aluno['Nome'] = input('Nome: ').strip().capitalize()
    while True:
        try:
            aluno['Média'] = float(input('Média: ').strip())
            break
        except ValueError:
            print('Digite apenas valores numéricos.')
    if aluno['Média'] < 7:
        aluno['Situação'] = 'Recuperação'.upper()
    elif aluno['Média'] >= 7:
        aluno['Situação'] = 'aprovado'.upper()
    for k, v in aluno.items():
        print(f'-{k} do aluno é {v}')
except KeyboardInterrupt:
    print()
    print('Interrompeu pelo teclado')
