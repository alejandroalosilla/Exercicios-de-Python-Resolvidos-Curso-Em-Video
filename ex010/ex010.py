#  Ex010 - Crie um programa que leia quanto dinheiro
# uma pessoa tem na carteira e mostre quantos dólares
# ela pode comprar.

r = float(input('Dinheiro em real: '))
d = r / 3.27
print('O valor {:.2f}R$ equivale a {:.2f}US$'.format(r, d))
