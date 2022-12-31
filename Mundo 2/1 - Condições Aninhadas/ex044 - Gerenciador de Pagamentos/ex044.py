#  Ex044 - Elabore um programa que calcule o valor a ser pago
# por um produto, considerando o seu preço normal e condição
# de pagamento:
# - Á vista dinheiro / cheque: 10% de desconto
# - Á vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print(20 * '=')
pp = float(input('Digite o preço do produto: '))
print(20 * '=')
print('Selecione a condição de pagamento: ')
print('[1] Á vista dinheiro / cheque')
print('[2] Á vista no cartão')
print('[3] Em até 2x no cartão')
print('[4] 3x ou mais no cartão')
e = int(input('=> '))
print(20 * '=')

if e == 1:
    pp = pp - (0.1 * pp)
    print('Preço Final: R${:.2f}'.format(pp))
elif e == 2:
    pp = pp - (0.05 * pp)
    print('Preço Final: R${:.2f}'.format(pp))
elif e == 3:
    print('Preço Final: R${:.2f}'.format(pp))
elif e == 4:
    pp = pp + (0.2 * pp)
    print('Preço Final: R${:.2f}'.format(pp))
else:
    print('\033[31mOpção incorreta!\033[m')
