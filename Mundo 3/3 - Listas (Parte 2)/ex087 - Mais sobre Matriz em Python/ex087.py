#  Ex087 - Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

l1 = list()
l2 = list()
l3 = list()

st = 0
sp = 0

c = 0
for e in range(0, 3):
    v = int(input(f'Digite um valor para [0, {e}]: '))
    l1.append(v)
    if v % 2 == 0:
        sp += v
    if c == 2:
        st += v
    c += 1

c = 0
for e in range(0, 3):
    v = int(input(f'Digite um valor para [1, {e}]: '))
    l2.append(v)
    if v % 2 == 0:
        sp += v
    if c == 2:
        st += v
    c += 1

c = 0
for e in range(0, 3):
    v = int(input(f'Digite um valor para [2, {e}]: '))
    l3.append(v)
    if v % 2 == 0:
        sp += v
    if c == 2:
        st += v
    c += 1

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

print('\n', 30 * '-=')
print(f'A soma dos valores pares é {sp}')
print(f'A soma dos valores da terceira coluna é {st}')
print(f'O maior valor da segunda linha é {max(l2)}')
