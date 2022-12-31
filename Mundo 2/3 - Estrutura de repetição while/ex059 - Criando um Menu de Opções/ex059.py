#  Ex059 - Crie um programa que leia dois valores e mostre um menu na
# tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
#  Seu programa deverá realizar a operação
# solicitada em cada caso.

from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

e = -1
while e != 5:
    print(20 * '=')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    e = int(input('=> '))

    if e == 1:
        s = n1 + n2
        print('Soma: {}'.format(s))
        sleep(2)
    elif e == 2:
        m = n1 * n2
        print('Multiplicação: {}'.format(m))
        sleep(2)
    elif e == 3:
        if n1 > n2:
            maior = n1
            print('Maior: {}'.format(maior))
            sleep(2)
        elif n2 > n1:
            maior = n2
            print('Maior: {}'.format(maior))
            sleep(2)
        elif n1 == n2:
            print('Não há maior!')
            sleep(2)
    elif e == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    print('Fim do programa!')
