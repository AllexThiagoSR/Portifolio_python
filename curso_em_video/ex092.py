from datetime import datetime
pessoa = dict()
pessoa['Nome'] = input('Nome: ').strip().capitalize()
while True:
    try:
        nascimento = int(input('Ano de nascimento: ').strip())
        pessoa['Idade'] = datetime.today().year - nascimento
        carteira = int(input('Carteira de trabalho (0 - não tem): ').strip())
        if carteira != 0:
            pessoa['CTPS'] = carteira
            pessoa['Ano de contratação'] = int(input('Ano de contratação: ').strip())
            pessoa['Aposentadoria'] = (pessoa['Ano de contratação'] - nascimento) + 35
            pessoa['Salário'] = 'R$ ' + str(float(input('Salário R$: ').strip()))
        else:
            pessoa['CTPS'] = 'Não tem'
        break
    except ValueError:
        print('Digite apenas números')
for k, v in pessoa.items():
    print(f'-O {k} tem o valor {v}')
