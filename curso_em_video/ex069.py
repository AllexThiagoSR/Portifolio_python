
from copy import deepcopy
pessoas = []
pessoa = dict()
seixo = ''
i = 0
analiz = {'Maiores de idade': 0, 'Homens': 0, 'Mulheres com menos de 20 anos': 0}
while True:
    while True:
        idade = input(f'Digite a idade {i + 1}ª pessoa: ').strip()
        try:
            idade = int(idade)
            pessoa['idade'] = idade
            break
        except ValueError:
            print('Digite apenas números.')
    seixo = 'a'
    while seixo not in 'MmFf':
        seixo = input('Qual o sexo dessa pessoa? [F/M]').strip().upper()[0]
    pessoa['sexo'] = seixo
    pessoas.append(deepcopy(pessoa))
    i += 1
    pessoa.clear()
    cont = '0'
    print('=' * 100)
    while cont not in 'SsNn':
        cont = input('Cadastrar mais uma pessoa? [S/N] ').strip().upper()[0]
        print()
    if cont in 'Ss':
        print('Continua')
        continue
    print('Encerra')
    break
print(i)
pessoas = (p for p in pessoas)
for j in pessoas:
    if j['idade'] >= 18:
        analiz['Maiores de idade'] += 1
    if j['idade'] < 20 and j['sexo'] == 'F':
        analiz['Mulheres com menos de 20 anos'] += 1
    if j['sexo'] == 'M':
        analiz['Homens'] += 1
for k, v in analiz.items():
    print(f'Das {i} pessoas cadastradas, {v} são {k}. '
          f'Que correspodem a {(v * 100) / i}% das pessoas cadastradas.')
