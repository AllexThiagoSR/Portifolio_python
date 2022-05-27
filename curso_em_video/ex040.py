from funverinu import is_number
n1 = input('Digite a primeira nota do aluno: ').strip()
n2 = input('Digite a segunda nota do aluno: ').strip()
if is_number(n1) and is_number(n2):
    n1 = float(n1)
    n2 = float(n2)
    med = (n1 + n2) / 2
    if med < 5:
        print(f'Com a média {med:.2f} você está, REPROVADO')
    elif 5 <= med <= 6.9:
        print(f'Com a média {med:.2f} você está, DE RECUPERAÇÃO')
    elif med >= 7:
        print(f'Com a média {med:.2f} você está, APROVADO')
else:
    print('Apenas números por favor')
