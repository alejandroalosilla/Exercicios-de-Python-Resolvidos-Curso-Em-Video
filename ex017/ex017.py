#  Ex017 - Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.
from math import sqrt
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))

h = sqrt((pow(co, 2)) + (pow(ca, 2)))
print('Hipotenusa: {:.2f}'.format(h))
