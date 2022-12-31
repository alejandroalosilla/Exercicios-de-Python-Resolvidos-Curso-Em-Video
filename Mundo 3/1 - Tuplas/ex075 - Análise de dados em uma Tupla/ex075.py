#  Ex075 - Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
v = (n1, n2, n3, n4)
print(f'Você digitou os valores: {v}')
print(f'O valor 9 apareceu {v.count(9)} vezes')


for pos, valor in enumerate(v):
    if valor == 3:
        print(f'O valor 3 apareceu na {pos + 1}ª posição')
        break
    if valor != 3 and pos == 3:
        print('O valor 3 não foi digitado em nenhuma posição')

print(f'O valores pares digitados foram ', end='')

for valor in v:
    if valor % 2 == 0:
        print(valor, end=' ')
