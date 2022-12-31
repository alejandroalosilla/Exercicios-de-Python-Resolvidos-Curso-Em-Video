#  Ex076 - Crie um programa que tenha uma tupla única com nomes de
# produtos e seus respectivos preços, na sequência.
#  No final, mostre uma listagem de preços, organizando os
# dados em forma tabular.

lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print(50 * '-')
print('          LISTAGEM DE PREÇOS')
print(50 * '-')

for p in range(0, len(lista)):
    if p % 2 == 0:
        print(f'{lista[p]:.<40}', end=' ')
    else:
        print(f'R${lista[p]:.2f}')
print(50 * '-')
