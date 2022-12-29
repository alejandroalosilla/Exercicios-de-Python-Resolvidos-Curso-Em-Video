#  Ex051 - Desenvolva um programa que leia o primeiro termo e a
# razão de uma PA.
#  No final, mostre os 10 primeiros termos dessa progressão.

print(20 * '=')
print('Progressão Aritmética!')
print(20 * '=')

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))


for c in range(1, 11):
    if c == 1:
        print('1º termo: {}'.format(p))
    else:
        print('{}º termo: {}'.format(c, p + r))
        p += r
