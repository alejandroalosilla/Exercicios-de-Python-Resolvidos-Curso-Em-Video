#  Ex100 - Faça um programa que tenha uma lista chamada números e duas
# funções chamadas sorteia() e somapar().
#  A primeira função vai sortear 5 números e vai colocá-los dentro
# da lista e a segunda função vai mostrar a soma entre todos os
# valores PARES sorteados pela função anterior.

from random import randint
from time import sleep

numeros = list()


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 9)
        numeros.append(n)
        print(n, end=' ')
        sleep(0.4)
    print('PRONTO!')


def somapar():
    sp = 0
    for c in numeros:
        if c % 2 == 0:
            sp += c
    print(f'Somando os valores pares de {numeros}, temos {sp}')


sorteia()
somapar()
