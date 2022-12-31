#  Ex062 - Melhore o DESAFIO 061, perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerra quando ele
# disser que quer mostrar Os termos.

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
ct = 1
e = 1
print('{} -> '.format(p), end='')

while e != 0:
    while c < 10:
        if c == 9:
            print('{} -> PAUSA'.format(p + r), end='')
        else:
            print('{} -> '.format(p + r), end='')
        p += r
        c += 1
        ct += 1
    e = int(input('\nQuantos termos você quer mostrar mais? '))
    c -= e

print('Progressão finalizada com {} termos mostrados!'.format(ct))
