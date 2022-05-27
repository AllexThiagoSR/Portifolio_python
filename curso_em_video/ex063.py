from funverinu import is_int
from ex062 import converte
print('=' * (len('  SEQUÊNCIA DE FIBONACCI') + 2))
print('  SEQUÊNCIA DE FIBONACCI')
print('=' * (len('  SEQUÊNCIA DE FIBONACCI') + 2))
termos = 0
while True:
    termos = input('Quantos termos deseja ver? ').strip()
    if is_int(termos):
        termos = int(termos)
        break
    print()
    print('Digite apenas números por favor')
    #continue
fib = 0
i = 1
t1 = 0
t2 = 1
while i <= termos:
    t1 = t2
    t2 = fib
    fib = t1 + t2
    print(fib, end=' -> ')
    if i == termos:
        print('PAUSA')
        termos += converte(input('Quantos termos a mais deseja ver? (0 se não quiser mais nenhum)').strip())
    i += 1

print('FIM')
