nota = []
for i in range(0, 2):
    nota.append(float(input(f'Digite a {i + 1}ª nota do aluno: ')))
for i in range(0, 2):
    print(f'{i + 1}ª nota: {nota[i]}')
print(f'A média do aluno foi: {(nota[0] + nota[1])/len(nota)}')
