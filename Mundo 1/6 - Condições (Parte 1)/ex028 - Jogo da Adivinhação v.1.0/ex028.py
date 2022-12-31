#  Ex028 - Escreva um programa que faça o computador "pensar" em um
# número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
#  O programa deverá escrever na tela se o usuário venceu
# ou perdeu.

from random import randint

nc = randint(0, 5)

ne = int(input('Tente advinhar um número entre 0 - 5: '))

if ne == nc:
    print('Você acertou! O número era {}!'.format(nc))
else:
    print('Você errou! O número era {}!'.format(nc))
