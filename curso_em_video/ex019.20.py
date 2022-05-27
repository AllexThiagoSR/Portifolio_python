from random import choice, shuffle

n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do aluno: '))
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno: '))
alu = [n1, n2, n3, n4]
shuffle(alu)
print(f'O aluno escolhido foi: {choice(alu)}')
print(f'Ou a ordem será: {alu}')
