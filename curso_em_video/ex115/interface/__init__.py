def linha(tam=42):
    return '=' * tam


def header(texto='SISTEMA ARQUIVO v1.0'):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(*args):
    from ex113 import leiaint
    header('MENU PRINCIPAL')
    opc = 0
    for i in range(0, len(args), 1):
        print(f'\033[33m{i + 1}\033[m - \033[34m{args[i]}\033[m')
    print(linha())
    try:
        opc = leiaint('\033[32mSua opção: \033[m')
        return args[opc - 1], opc
    except (IndexError, TypeError):
        return '', opc
