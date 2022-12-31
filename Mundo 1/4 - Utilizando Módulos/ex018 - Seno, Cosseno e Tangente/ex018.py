#  Ex018 - Faça um programa que leia um ângulo qualquer e mostre
# na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

a = float(input('Digite um ângulo: '))

print('Seno de {}: {:.2f}'.format(a, sin(radians(a))))
print('Cosseno de {}: {:.2f}'.format(a, cos(radians(a))))
print('Tangente de {}: {:.2f}'.format(a, tan(radians(a))))
