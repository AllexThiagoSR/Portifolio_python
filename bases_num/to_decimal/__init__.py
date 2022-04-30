def bin2dec(val='0', show=False):
    val = val.replace(' ', '')
    val_inv = val[-1::-1]
    resu = 0
    for i in range(len(val) - 1, -1, -1):
        try:
            j = int(val_inv[i])
            if j > 1:
                raise ValueError('Não valores maiores que 1 na base binária')
            resu += j * (2 ** i)
        except ValueError:
            raise
    return (resu, val) if show else resu


def hex2dec(val='0', show=False):
    hexa = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    resu = 0
    val = val.upper().replace(' ', '')
    val_inv = val[-1::-1]
    for i in range(len(val) - 1, -1, -1):
        if val[i] not in hexa:
            raise IndexError('Não há esse caractere na base hexadecimal')
        resu += hexa.index(val_inv[i]) * (16 ** i)
    return (resu, val) if show else resu


def oct2dec(val='0', show=False):
    val = val.replace(' ', '')
    val_inv = val[-1::-1]
    resu = 0
    for i in range(len(val_inv) - 1, -1, -1):
        try:
            j = int(val_inv[i])
            if j > 8:
                raise ValueError('Não há valores maiores que 8 na base octal.')
            resu += j * (8 ** i)
        except ValueError:
            raise
    return (resu, val) if show else resu
