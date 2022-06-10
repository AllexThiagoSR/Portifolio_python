class User:
    from the_book_is_on_the_table.inventario import Livro

    def __init__(self, nome, usuario, senha):
        self.nome = nome
        self.usuario = usuario
        self.senha = senha
        self.livros = []

    def mudar_usuario(self):
        pass

    def mudar_senha(self):
        pass

    def pegar_livro(self, nome_livro, quantidade):
        for livro in self.livros:
            if livro.nome == nome_livro:
                livro.quantidade += quantidade
                break
        else:
            self.livros.append(self.Livro(nome_livro, quantidade))

    def devolver_livro(self, nome_livro):
        for i in self.livros:
            if i.nome == nome_livro:
                self.livros.remove(i)
                break
        else:
            print('Não há livros para devolução.')


def empresta(users):
    with open('livros_emprestados.txt', 'w') as file:
        for user in users:
            file.write(f'{user.nome}')
            for livro in user.livros:
                file.write(f';{livro.nome}|{livro.quantidade}')
            file.write('\n')


def logar(usuario, senha, users):
    for user in users:
        if usuario == user.usuario and senha == user.senha:
            print('Logado com sucesso!!!')
            return [True, users.index(user)]
        elif usuario == user.usuario and senha != user.senha:
            print('Senha incorreta...Voltando para o menu principal.')
            return [False, '']
    else:
        print('Não há esse usuário.')
        return [False, '']


def cadastra(nome, usuario, senha):
    with open('users.txt', 'a') as file:
        file.write(f'{nome};{usuario};{senha}\n')
    return User(nome=nome, usuario=usuario, senha=senha)
