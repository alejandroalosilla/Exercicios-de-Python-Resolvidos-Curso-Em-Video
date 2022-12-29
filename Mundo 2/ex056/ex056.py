#  Ex056 - Desenvolva um programa que leia o nome, idade e sexo de
# 4 pessoas. 
#  No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

si = 0
mi = 0
nv = ''
mvi = 0

for c in range(1, 5):
    n = str(input('Nome da {}° pessoa: '.format(c))).strip()
    i = int(input('Idade da {}° pessoa: '.format(c)))
    s = str(input('Sexo da {}° pessoa [m/f]: '.format(c))).strip().upper()

    si += i

    if i > mi:
        mi = i
        nv = n
    if s == 'F' and i < 20:
        mvi += 1

print('Média de idade: {}'.format(si / 4))
print('Nome do homem mais velho: {}'.format(nv))
print('Mulheres com menos de 20 anos: {}'.format(mvi))
