#  Ex060 - Faça um programa que leia um número qualquer e mostre
# o seu fatorial.
# EX: 5! = 5X4X3X2X1 = 120

n = int(input('Digite um número: '))
b = 0
c = 0
f = n
nn = n

while c < n + 1:
    f = f * (n - 1)
    n -= 1
    c += 1

print('Calculando {}! = '.format(nn), end='')
while b < nn:
    if nn == 1:
        print('1 = {}'.format(f), end='')
    else:
        print('{} x '.format(nn), end='')
    nn -= 1
