#  Ex023 - Faça um programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos dígitos separados.
# EX:
# Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

n = int(input('Digite um número de 0 - 9999: '))
# 1234
u = n % 10
d = (n // 10) % 10
c = (n // 100) % 10
m = (n // 1000) % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
