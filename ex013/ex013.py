#  Ex013 - Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o salário: '))
ns = s + (0.15 * s)
print('O novo salário com 15% de aumento é: {:.2f}R$'.format(ns))
