#  Ex086 - Crie um programa que crie uma matriz de dimensão 3x3 e
# preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com a formatação
# correta.

l1 = list()
l2 = list()
l3 = list()

for c in range(0, 3):
    l1.append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    l2.append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    l3.append(int(input(f'Digite um valor para [2, {c}]: ')))
print(30 * '-=')


for e in l1:
    print(f'[ {e} ]', end='')

c = 0
for e in l2:
    if c == 0:
        print(f'\n[ {e} ]', end='')
    else:
        print(f'[ {e} ]', end='')
    c += 1

c = 0
for e in l3:
    if c == 0:
        print(f'\n[ {e} ]', end='')
    else:
        print(f'[ {e} ]', end='')
    c += 1
