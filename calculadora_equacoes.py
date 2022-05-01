def calculator(equacao=''):
    """
    Calculadora de equações simples, com as operações: adição, subtração, divisão e multiplicação
    Não calcula equações com incógnitas
    :param equacao: Uma string com a equação deve ser passada
    :return: retorna o resultado da equação.
    """
    for i in range(0, len(equacao), 1):
        if equacao[i] in 'qwertyuiopasdfghjklçzxcvbnm$#@!&()°ºª][{}?:;|':
            raise ValueError('Não pode haver letras ou caracteres especiais.')
    equacao = equacao.strip().replace('', ' ').split()
    string = ''
    for i in range(len(equacao) - 1, -1, -1):
        if equacao[i] in '+-*/':
            equacao.insert(i + 1, ' ')
            equacao.insert(i, ' ')
    for i in equacao:
        string += i
    equacao = string.split()
    i = 0
    while i < len(equacao):
        if equacao[i] == '*':
            equacao[i] = str(float(equacao[i - 1]) * float(equacao[i + 1]))
            del equacao[i + 1]
            del equacao[i - 1]
            i = -1
        elif equacao[i] == '/':
            equacao[i] = str(float(equacao[i - 1]) / float(equacao[i + 1]))
            del equacao[i + 1]
            del equacao[i - 1]
            i = -1
        i += 1
    i = 0
    while i < len(equacao):
        if equacao[i] == '+':
            equacao[i] = str(float(equacao[i - 1]) + float(equacao[i + 1]))
            del equacao[i + 1]
            del equacao[i - 1]
            i = -1
        elif equacao[i] == '-':
            equacao[i] = str(float(equacao[i - 1]) - float(equacao[i + 1]))
            del equacao[i + 1]
            del equacao[i - 1]
            i = -1
        i += 1
    resu = float(equacao[0])
    return resu
