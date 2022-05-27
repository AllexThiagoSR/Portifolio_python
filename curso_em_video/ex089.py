from copy import deepcopy
boletins = list()  # lista
aluno = dict()
notas = []  # lista
print(f'Cadastrando alunos')
print('=' * 100)
while True:
    aluno['nome'] = input('Nome: ').strip().capitalize()
    for i in range(0, 2, 1):
        while True:
            try:
                no = float(input(f'Digite a {i + 1}ª nota: ').strip())
                if no <= 10:
                    break
                else:
                    print('A nota só pode ser menor ou igual a 10')
            except ValueError:
                print('Digite apenas valores númericos')
        notas.append(no)
    media = sum(notas) / len(notas)
    aluno['notas'] = notas[:]
    aluno['média'] = media
    boletins.append(deepcopy(aluno))
    print('Alunos cadastrado')
    aluno.clear()
    notas.clear()
    cont = 'a'
    print('=' * 100)
    while cont not in 'NnSs':
        cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
    print('=' * 100)
    if cont == 'N':
        break
print(f'{"No.":<4}|{"Nome":<15}|{"Média":<6}')
print('=' * len(f'{"No.":<4}|{"Nome":<15}|{"Média":<6}'))
for i in boletins:
    print(f'{boletins.index(i):<4} {i["nome"]:<15} {i["média"]:<6.2f}')
while True:
    print('=' * 100)
    while True:
        try:
            mostra = int(input('Mostrar informções de qual aluno? (999 - parar) ').strip())
            break
        except ValueError:
            print('Digite apenas valores numéricos')
    print('=' * 100)
    if mostra == 999:
        break
    try:
        print(f'Nome: {boletins[mostra]["nome"]}')
        for i in boletins[mostra]["notas"]:
            print(f'{boletins[mostra]["notas"].index(i) + 1}ª nota: {i:.2f}')
        print(f'Média: {boletins[mostra]["média"]:.2f}')
    except IndexError:
        print('Não há aluno cadastrado nessa posição')
print('Encerrou')
