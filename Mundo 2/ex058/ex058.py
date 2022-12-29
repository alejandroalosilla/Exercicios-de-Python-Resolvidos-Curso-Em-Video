#  Ex058 - Melhore o jogo do DESAFIO 028 onde o computador vai
# "pensar" em um número entre 0 e 10.
#  Só que agora o jogador vai tentar advinhar até acertar, mostrando
# no final quantos palpites foram necessários para vencer.

from random import randint

pc = randint(0, 10)
t = -1
nt = 0
while t != pc:
    t = int(input('Tente advinhar o número de 0-10: '))
    if t == pc:
        print('Você acertou! o número era {}!'.format(pc))
    else:
        nt += 1
        print('Tente novamente...')
print('Número de tentativas até acertar: {}'.format(nt))
