#  Ex063 - Escreva um programa que leia um número n inteiro
# qualquer e mostre na tela os n primeiros elementos
# de uma sequência de Fibonacci.
#  EX: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print(30 * '-')
print('Sequência de Fibonacci')
print(30 * '-')

nt = int(input('Quantos termos você quer mostrar? '))
print(30 * '=-')
c = 1
pt = 0
st = 1

print('{} -> {} -> '.format(pt, st), end='')
while c < nt - 1:
    tt = pt + st
    if c == nt - 2:
        print('{} -> FIM\n'.format(tt), end='')
    else:
        print('{} -> '.format(tt), end='')
    pt = st
    st = tt
    c += 1
print(30 * '=-')
