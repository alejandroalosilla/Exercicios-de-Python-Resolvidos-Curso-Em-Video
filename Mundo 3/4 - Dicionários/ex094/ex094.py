#  Ex094 - Crie um programa que leia nome, sexo e idade de várias
# pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista.
#  No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

lp = list()
lm = list()
dp = dict()
tp = 0
si = 0

while True:
    dp['Nome'] = str(input('Nome: ')).strip().capitalize()
    dp['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    if dp['Sexo'] == 'F':
        lm.append(dp['Nome'])
    dp['Idade'] = int(input('Idade: '))
    lp.append(dp.copy())
    tp += 1
    si += dp['Idade']
    dp.clear()

    option = ''
    while option != 'S' and option != 'N':
        option = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if option == 'N':
        break
mi = si / tp
print(30 * '-=')
print(f'- O grupo tem {tp} pessoas')
print(f'- A média de idade é de {mi:.2f} anos')
print(f'- As mulheres cadastradas foram: ', end='')
for c in lm:
    print(f'[{c}] ', end='')
print()
print('- Lista das pessoas que estão acima da média:')

for c in lp:
    if c['Idade'] > mi:
        print(f"nome = {c['Nome']}; sexo = {c['Sexo']}; idade = {c['Idade']}")
print('<< Encerrado >>')
