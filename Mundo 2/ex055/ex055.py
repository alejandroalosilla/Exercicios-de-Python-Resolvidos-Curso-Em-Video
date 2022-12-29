#  Ex055 - Faça um programa que leia o peso de cinco pessoas.
#  No final, mostre qual foi o maior e o menor peso
# lidos.

me = 1000
ma = 0

for c in range(1, 6):
    p = float(input('Peso da º{} pessoa: '.format(c)))
    if p > ma:
        ma = p
    elif p < me:
        mep = p
print('Maior peso: {}'.format(ma))
print('Menor peso: {}'.format(me))
