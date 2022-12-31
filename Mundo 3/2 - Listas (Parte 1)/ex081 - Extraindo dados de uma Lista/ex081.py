#  Ex081 - Crie um programa que vai ler vários números e colocar em
# uma lista.
#  Depois disso, mostre:
# A) Quantos números fora digitados.
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista.

ll = list()
c = 0

while True:
    ll.append(int(input('Digite um valor: ')))
    c += 1
    op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Você digitou {c} elementos.')
print(f'Os valores em ordem decrescente são {sorted(ll, reverse=True)}')
if 5 in ll:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
