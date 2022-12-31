#  Ex033 - Faça um programa que leia três números e mostre qual é
# o maior e qual é o menor.

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

# Testando o Maior:
ma = a
if b > a and b > c:
    ma = b
elif c > a and c > b:
    ma = c

# Testando o Menor:
me = a
if b < a and b < c:
    me = b
elif c < a and c < b:
    me = c
print('O menor número é {}!'.format(me))
print('O maior número é {}!'.format(ma))
