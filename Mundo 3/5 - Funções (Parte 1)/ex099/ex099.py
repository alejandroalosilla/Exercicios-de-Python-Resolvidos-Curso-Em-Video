#  Ex099 - Faça um programa que tenha uma função chamada maior(), que receba
# vários parâmetros com valores inteiros.
#  Seu programa tem que analisar todos os valores e dizer qual deles
# é o maior.

from time import sleep


def maior(*val):
    print(30 * '-=')
    print('Analisando os valores passados...')
    if len(val) != 0:
        for c in val:
            print(c, end=' ')
            sleep(0.4)
        print(f'Foram informados {len(val)} valores ao todo.')
        print(f'O maior valor informado foi {max(val)}')
    else:
        print(f'Foram informados 0 valores ao todo.')
        print(f'O maior valor informado foi 0')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
