#  Ex065 - Crie um programa que leia vários números inteiros
# pelo teclado.
#  No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos.
#  O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores


n = 0
ma = 0
me = ''
sn = 0
tn = 0
r = ''

while r != 'N':
    x = n = float(input('Digite um número: '))
    tn += 1
    sn += n

    if n > ma:
        ma = n
    if tn == 1:
        me = n
    if n < me:
        me = n


r = str(input('Quer continuar? [S/N]: ')).strip().upper()
m = sn / tn
print('Você digitou {} e a média foi {:.2f}'.format(tn, m))
print('O maior valor foi {} e o menor foi {}'.format(ma, me))
