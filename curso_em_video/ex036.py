from funverinu import is_number


def emprestimo(valor_casa=0.0, sala=0.0, anos=1.0):
    prest = valor_casa / (anos * 12)
    prest_vali = sala * 0.3
    if prest <= prest_vali:
        return f'A casa custa R${valor_casa:.2f}, para pagar em {anos} anos prestação mensal seria de R${prest:.2f} com o salário de R${sala:.2f} mensais você consegue pagar tranquilamente, empréstimo APROVADO'
    return f'A casa custa R${valor_casa:.2f}, para pagar em {anos} anos prestação mensal seria de R$ {prest:.2f} com o salário de R${sala:.2f} mensais vai ficar puxado pra você pagar, empréstimo NEGADO'


preco = input('Qual o preço da casa que deseja comprar: R$ ').strip()
salario = input('Quanto você ganha por mês? R$ ').strip()
tempo = input('Em quanto tempo deseja pagar esse financiamento? ').strip()
if is_number(preco) and is_number(salario) and is_number(tempo):
    preco = float(preco)
    salario = float(salario)
    tempo = float(tempo)
    print(emprestimo(valor_casa=preco, anos=tempo, sala=salario))
else:
    print('Digite apenas números por favor')
