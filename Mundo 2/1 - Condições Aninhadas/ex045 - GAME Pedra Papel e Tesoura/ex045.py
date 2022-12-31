#  Ex045 - Crie um programa que faça o computador jogar
# Jokenpô com você.

import random

c = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
print(20 * '=')
print('*Jokenpô*')
print(20 * '=')
print('Pedra, papel ou tesoura...')
p = str(input('=> ')).strip().upper()
print(20 * '=')

if p == c:
    print('{} x {} EMPATE!'.format(p, c))
elif p == 'PAPEL' and c == 'TESOURA':
    print('{} x {} COMPUTADOR VENCEU!'.format(p, c))
elif p == 'PAPEL' and c == 'PEDRA':
    print('{} x {} PLAYER VENCEU!'.format(p, c))
elif p == 'PEDRA' and c == 'PAPEL':
    print('{} x {} COMPUTADOR VENCEU!'.format(p, c))
elif p == 'PEDRA' and c == 'TESOURA':
    print('{} x {} PLAYER VENCEU!'.format(p, c))
elif p == 'TESOURA' and c == 'PEDRA':
    print('{} x {} COMPUTADOR VENCEU!'.format(p, c))
elif p == 'TESOURA' and c == 'PAPEL':
    print('{} x {} PLAYER VENCEU!'.format(p, c))
else:
    print('\033[31mOPÇÃO ERRADA!\033[m')
