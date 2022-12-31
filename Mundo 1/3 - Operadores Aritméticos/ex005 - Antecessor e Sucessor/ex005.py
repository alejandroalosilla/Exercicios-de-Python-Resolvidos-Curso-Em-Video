#  Ex005 - Faça um programa que leia um número inteiro e mostre
# na tela o seu sucessor e o seu antecessor.

n = int(input('Digite um número inteiro: '))

suc = n + 1
ant = n - 1

print('O sucessor de {} é {}'.format(n, suc), end=' ')
print('e o antecessor é {}!'.format(ant))
