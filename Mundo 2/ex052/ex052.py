#  Ex052 - Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

print(20 * '=')
print('Descobrindo números primos!')
print(20 * '=')
n = int(input('Digite um número inteiro: '))
tot = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[36m{}'.format(c), end=' ')
        tot += 1
    else:
        print('\033[31m{}'.format(c), end=' ')

print('\n\033[33mO número {} foi divisível {} vezes!'.format(n, tot))

if tot == 2:
    print('\033[32mO número {} É PRIMO!'.format(n))
else:
    print('\033[31mO número {} NÃO É PRIMO!'.format(n))
