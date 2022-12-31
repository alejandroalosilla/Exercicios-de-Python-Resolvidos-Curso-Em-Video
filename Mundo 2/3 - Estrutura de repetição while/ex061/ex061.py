#  Ex061 - Refaça o DESAFIO 051, lendo o primeiro termo e a razão
# de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
print('{} -> '.format(p), end='')
while c < 10:
    if c == 9:
        print('{} -> FIM'.format(p + r), end='')
    else:
        print('{} -> '.format(p + r), end='')
    p += r
    c += 1
