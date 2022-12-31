#  Ex088 - Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.
#  O programa vai perguntar quantos jogos serão gerados e vai
# sortear 6 números entre 1 e 60 para cada jogo, cadastrando
# tudo em uma lista composta.

from time import sleep
from random import randint
lj = list()

print(30 * '-')
print(' JOGAR NA MEGA SENA')
print(30 * '-')

n = int(input('Quantos jogos você quer que eu sorteie? '))
print(5 * '-=', f'SORTEANDO {n} JOGOS', 5 * '-=')
for c in range(1, n + 1):
    for e in range(0, 6):
        while True:
            v = randint(1, 60)
            if v not in lj:
                lj.append(v)
                break
    print(f'Jogo {c}: {lj}')
    sleep(1)
    lj.clear()
print(5 * '-=', '< BOA SORTE! >', 5 * '-=')
