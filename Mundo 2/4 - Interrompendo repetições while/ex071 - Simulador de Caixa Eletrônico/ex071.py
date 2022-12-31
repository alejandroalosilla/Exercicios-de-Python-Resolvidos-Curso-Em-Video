#  Ex071 - Crie um programa que simule o funcionamento de um
# caixa eletrônico.
#  No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai
# informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de
# - R$ 50
# - R$ 20
# - R$ 10
# - R$ 1

t50 = 0
t20 = 0
t10 = 0
t1 = 0

print(30 * '=')
print('          BANCO CEV')
print(30 * '=')

while True:
    v = int(input('Qual valor você quer sacar? R$'))
    if v == 0:
        print('Nenhum valor foi solicitado!')
        break

    t50 = v // 50
    print(f'Total de {t50} cédulas de R$50')
    if v % 50 == 0:
        break
    else:
        v = v % 50

    t20 = v // 20
    print(f'Total de {t20} cédulas de R$20')
    if v % 20 == 0:
        break
    else:
        v = v % 20

    t10 = v // 10
    print(f'Total de {t10} cédulas de R$10')
    if v % 10 == 0:
        break
    else:
        v = v % 10

    t1 = v // 1
    print(f'Total de {t1} cédulas de R$1')
    print(30 * '=')
    if v % 1 == 0:
        break

print('Tenha um um bom dia!')
