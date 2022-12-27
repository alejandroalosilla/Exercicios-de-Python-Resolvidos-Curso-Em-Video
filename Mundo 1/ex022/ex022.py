#  Ex022 - Crie um programa que leia o nome completo de uma pessoa
# e mostre:
# -> O nome com todas as letras maiúsculas.
# -> O nome com todas minúsculas.
# -> Quantas letras ao todo( sem considerar espaços).
# -> Quantas letras tem o primeiro nome

n = str(input('Digite um nome: ')).strip()
print('Todas as letras maiúsculas: {}'.format(n.upper()))
print('Todas as letras minúsculas: {}'.format(n.lower()))
print('Número de letras: {}'.format(len(n) - n.count(' ')))
ns = n.split()
print('O primeiro nome tem {} letras!'.format(len(ns[0])))
