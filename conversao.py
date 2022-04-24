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
    for i in range(len(bi) - 1, -1, -1):
        ib += bi[i]
    return (ib, num) if show else ib


def hexadecimal(num=0, show=False):
    """
    Função para conversão de números da base decimal para a base hexadecimal
    :param num: Valor que deseja converter
    :param show: Se deseja mostrar o resultado da conversão e o número que foi convertido
    :return: Se "show" for igual a True retorna uma tupla com o resultado da conversão e o número que foi convertido,
    se não retorna o resultado da conversão
    """
    alga = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    he = ''
    hey = '0x'
    q = num
    if num < 16:
        he += alga[num]
    elif num >= 16:
        while True:
            r = q % 16
            q = q // 16
            if q < 16:
                he += alga[r]
                he += alga[q]
                break
            elif q >= 16:
                he += alga[r]
    for i in range(len(he) - 1, -1, -1):
        hey += he[i]
    return (hey, num) if show else hey
