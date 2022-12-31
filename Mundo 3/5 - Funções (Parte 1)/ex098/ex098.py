#  Ex098 - Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo e realize
# a contagem.
#  Seu programa tem que realizar três contagens através da
# função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada

from time import sleep


def p():
    print(30 * '-=')


def c1_10():
    sleep(1)
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.4)
    print('FIM!')


def c10_0():
    sleep(1)
    for c in range(10, -1, -2):
        print(c, end=' ')
        sleep(0.4)
    print('FIM!')


def c_p(i1, f1, p1):
    sleep(1)
    if p1 == 0:
        p1 = 1
    if i1 < f1:
        for c in range(i1, f1 + 1, p1):
            print(c, end=' ')
            sleep(0.4)
        print('FIM!')
    if i1 > f1:
        for c in range(i1, f1 - 1, -1 * p1):
            print(c, end=' ')
            sleep(0.4)
        print('FIM!')


p()
print('Contagem de 1 até 10 de 1 em 1')
c1_10()
p()
print('Contagem de 10 até 0 de 2 em 2')
c10_0()
p()
print('Agora e sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = abs(int(input('Passo: ')))
c_p(i, f, p)
