nome = str(input('Digite seu nome: '))
print(f'Nome com todas as letras em maiúsculo: {nome.upper()}')
print(f'Nome com todas as letras em minúsculo: {nome.lower()}')
print(f'A quantidade de letras do nome inteiro: {len(nome.replace(" ", ""))}')
nome = nome.split()
print(f'Quantidade de letras do primeiro nome: {len(nome[0])}')
