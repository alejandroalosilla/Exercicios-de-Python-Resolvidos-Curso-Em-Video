#  Ex083 - Crie um programa onde o usuário digite uma expressão
# qualquer que use parênteses.
#  Seu aplicativo deverá analisar se a expressão passada está com os
# parênteses abertos e fechados na ordem correta.

e = str(input('Digite a expressão: ')).strip().replace(' ', '')
ll = list()

for c in range(0, len(e)):
    ll.append(e[c])

s = ll.count('(') + ll.count(')')

if s % 2 == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
