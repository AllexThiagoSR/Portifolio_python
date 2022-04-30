def binario(num=0, show=False):
    """
    Função para conversão de números da base decimal para a base binária
    :param num: Valor que deseja converter
    :param show: Se deseja mostrar o resultado da conversão e o número que foi convertido
    :return: Se "show" for igual a True retorna uma tupla com o resultado da conversão e o número que foi convertido,
    se não retorna o resultado da conversão
    """
    bi = ''
    ib = '0b'
    if num > 1:
        op = num
        while True:
            if op < 2:
                bi += f'{op % 2}'
                break
            elif op % 2 == 1:
                bi += '1'
            elif op % 2 == 0:
                bi += '0'
            op = op // 2
    else:
        bi += '1' if num == 1 else '0'
    ib += bi[-1::-1]
    return (ib, num) if show else ib
