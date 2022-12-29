#  Ex054 - Crie um programa que leia o ano de nascimento de sete
# pessoas.
#  No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas ja são maiores.

import datetime
aa = datetime.datetime.now()
ano = aa.year

ma = 0
me = 0

for c in range(1, 8):
    an = int(input('Ano de nascimento da {}º pessoa: '.format(c)))
    if (ano - an) < 18:
        me += 1
    else:
        ma += 1
print('Pessoas maiores de idade: {}'.format(ma))
print('Pessoas menores de idade: {}'.format(me))
