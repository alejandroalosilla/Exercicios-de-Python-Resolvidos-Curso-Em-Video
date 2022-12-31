#  Ex070 - Crie um programa que leia o nome e o preço de
# vários produtos.
#  O programa deverá perguntar se o usuário vai continuar.
#  No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

c = 0  # Contador
tc = 0  # Total da Compra
pm = 0  # Produto maior que MIL
nb = ''  # Nome do produto Mais Barato
pb = 0  # Preço do mais Barato

print(40 * '-')
print('LOJA SUPER BARATÃO')
print(40 * '-')

while True:
    n = str(input('Nome do Produto: ')).strip()
    p = int(input('Preço: R$'))

    c += 1
    tc += p

    if p > 1000:
        pm += 1

    if c == 1:
        nb = n
        pb = p

    if p < pb:
        pb = p
        nb = n

    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if r == 'S' or r == 'N':
            break
    if r == 'N':
        break

print('------ FIM DO PROGRAMA ------')
print(f'O total da compra foi R${tc:.2f}')
print(f'Temos {pm} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nb} que custa R${pb:.2f}')
