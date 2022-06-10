class Livro:
    def __init__(self, nome, quantidade=1):
        self.nome = nome
        self.quantidade = quantidade

    def pegar(self, q=1):
        if q <= self.quantidade:
            self.quantidade -= q
        else:
            print('Não temos estoque para isso.')

    def devolver(self, q=1):
        self.quantidade += q


def mostrar_inv(livros):
    print('-' * 50)
    print(f'No. {"Nome":<43}{"Qt.":>3}')
    print('-' * 50)
    if len(livros) == 0:
        print('Sem livros para devolução.')
    else:
        for j, i in enumerate(livros):
            print(f'{j} - {i.nome:.<43}{i.quantidade:>3}')
    print('-' * 50)


def atualiza(livros):
    with open('livros.txt', 'w') as file:
        for i in livros:
            file.write(f'{i.nome};{i.quantidade}\n')
