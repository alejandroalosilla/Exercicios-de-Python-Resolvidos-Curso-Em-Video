#  Ex074 - Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla.
#  Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.

from random import randint

t = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
ts = sorted(t)
print(f'Os valores sorteados foram: {t[0]} {t[1]} {t[2]} {t[3]} {t[4]}')
print(f'O maior valor sorteado foi {ts[4]}')
print(f'O menor valor sorteado foi {ts[0]}')
