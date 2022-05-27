def mostrar(arquivo='generico.txt'):
    with open(arquivo, 'rt') as file:
        st = file.read()
        file.seek(0, 0)
        if not st == 'Não há pessoas cadastradas.':
            for i in file.readlines():
                j = i.replace('\n', '').split(';')
                print(f'{j[0]:<34}{j[1]:>3} anos')
                print('_' * 42)
        else:
            print(file.read())


def cadastrar(nome='<desconhecido>', idade=0, arquivo='generico.txt'):
    from os import remove
    with open(arquivo, 'rt') as file:
        st = file.read()
    remove(arquivo) if st == 'Não há pessoas cadastradas.' else ...
    with open(arquivo, 'at') as file:
        file.write(f'{nome};{idade}\n')
        with open('cadastro.txt', 'at') as f:
            f.write(f'{nome:<34}{idade:>3} anos\n')
            f.write('_' * 42)
            f.write('\n')


def criararq(arquivo='generico.txt'):
    from time import sleep
    try:
        with open(arquivo, 'rt+') as file:
            file.read()
    except FileNotFoundError:
        print('Arquivo não existente.')
        print('Criando arquivo.')
        with open(arquivo, 'wt+') as file:
            file.write('Não há pessoas cadastradas.')
        sleep(2)
        print('Criado!!!')
