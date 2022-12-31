#  Ex053 - Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando
# os espaços.
# Ex: APOS A SOPA

f = str(input('Digite uma frase qualquer: ')).strip().upper()
f = f.replace(' ', '')
v = ''

for c in range(len(f) - 1, -1, -1):
    print(f[c], end='')
    v = v + f[c]

if f == v:
    print('\nÉ um palíndromo!')
else:
    print('\nNão é um palíndromo!')
