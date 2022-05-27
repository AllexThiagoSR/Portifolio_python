from copy import deepcopy
pessoa = dict()
pessoas = list()
molieres = list()
idade_maior = list()
media = 0
while True:
    pessoa['Nome'] = input('Nome: ').strip().title()
    pessoa['Sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
    while True:
        try:
            pessoa['Idade'] = int(input('Idade: ').strip())
            media += pessoa['Idade']
            break
        except ValueError:
            print('Digite apenas números.')
    pessoas.append(deepcopy(pessoa))
    pessoa.clear()
    cont = 'a'
    print('=' * 100)
    while cont not in 'NnSs':
        cont = input('Deseja continuar? (S/N) ').strip().upper()[0]
    print('=' * 100)
    if cont == 'N':
        break
media = media / len(pessoas)
pessoas.append(media)
for i in pessoas:
    try:
        if i['Sexo'] == 'F':
            molieres.append(i['Nome'])
        if i['Idade'] > pessoas[-1]:
            idade_maior.append(i['Nome'])
    except Exception:
        pass
print(f'{len(pessoas) - 1} pessoas foram cadastradas')
print(f'A média de idade é {pessoas[-1]:.2f}')
print(f'Mulheres cadastradas: {molieres}')
print(f'Pessoas com idade maior que a média: {idade_maior}')
