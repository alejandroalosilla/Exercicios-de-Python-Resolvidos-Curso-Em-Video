#  Ex084 - Faça um programa que leia o nome e peso de várias pessoas,
# guardando tudo em uma lista.
#  No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

galera = list()
dado = list()
totp = 0
mp = 0
men = 0

while True:
    dado.append(str(input('Nome: ')).strip())
    dado.append(int(input('Peso: ')))
    galera.append(dado[:])

    if totp == 0:
        mp = dado[1]
        men = dado[1]
    if totp > 0 and dado[1] > mp:
        mp = dado[1]
    if totp > 0 and dado[1] < men:
        men = dado[1]

    dado.clear()
    totp += 1

    option = ''
    while option != 'N' and option != 'S':
        option = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if option == 'N':
        break
print(30 * '-=')
print(f'Ao todo, você cadastrou {totp} pessoas.')
print(f'O maior peso foi de {mp}Kg. Peso de ', end='')

for c in range(0, len(galera)):
    if galera[c][1] == mp:
        print(f'[{galera[c][0]}]', end=' ')

print(f'\nO menor peso foi de {men}Kg. Peso de ', end='')

for c in range(0, len(galera)):
    if galera[c][1] == men:
        print(f'[{galera[c][0]}]', end=' ')
