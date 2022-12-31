#  Ex078 - Faça um programa que leia 5 valores numéricos e guarde-os
# em uma lista.
#  No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.

ll = list()

for c in range(0, 5):
    ll.append(int(input(f'Digite um valor para a posição {c}: ')))
print(40 * '=-')
print(f'Você digitou os valores {ll}')


print(f'O maior valor digitado foi {max(ll)} nas posições ', end='')
for pos, num in enumerate(ll):
    if num == max(ll):
        print(f'{pos}...', end=' ')

print(f'\nO menor valor digitado foi {min(ll)} nas posições ', end='')
for pos, num in enumerate(ll):
    if num == min(ll):
        print(f'{pos}...', end=' ')
