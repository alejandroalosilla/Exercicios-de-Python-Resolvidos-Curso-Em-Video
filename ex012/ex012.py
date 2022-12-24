#  Ex012 - Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o preço do produto: '))
np = p - (0.05 * p)
print('O novo preço com 5% de desconto é: {:.2f}R$'.format(np))
