#  Ex035 - Desenvolva um programa que leia o comprimento de três
# retas e diga ao usuário se elas podem ou não formar um
# triângulo.

a = float(input('Comprimento a: '))
b = float(input('Comprimento b: '))
c = float(input('Comprimento c: '))

if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    print('As medidas formam um triângulo!')
else:
    print('As medidas não formar um triângulo!')
