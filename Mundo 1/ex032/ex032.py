#  Ex032 - Faça um programa que leia um ano qualquer e mostre
# se ele é BISSEXTO.

a = int(input('Digite um ano: '))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(a))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(a))
