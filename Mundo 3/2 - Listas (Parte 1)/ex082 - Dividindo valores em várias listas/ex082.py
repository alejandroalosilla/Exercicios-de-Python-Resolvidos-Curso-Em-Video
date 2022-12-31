#  Ex082 - Crie um programa que vai ler vários números e colocar em
# uma lista.
#  Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente.
#  Ao final, mostre o conteúdo das três listas geradas.

l1 = list()
lp = list()
li = list()

while True:
    l1.append(int(input('Digite um número: ')))
    op = str(input('Quer continuar? [N/S]: ')).strip().upper()[0]

    if op == 'N':
        break
for v in range(0, len(l1)):
    if l1[v] % 2 == 0:
        lp.append(l1[v])
    else:
        li.append(l1[v])
print(f'A lista completa é {l1}')
print(f'A lista de pares é {lp}')
print(f'A lista de ímpares é {li}')
