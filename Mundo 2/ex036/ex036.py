#  Ex036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma
# casa.
#  O programa vai perguntar o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar.
#  Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
# do salário ou então o empréstimo será negado.

vc = float(input('Qual o valor da casa? '))
sc = float(input('Qual o salário do comprador? '))
a = int(input('Quantos anos para pagar? '))

pm = vc / (a * 12)

if pm > (0.3 * sc):
    print('Salário: R${:.2f}'.format(sc))
    print('Prestação: R${:.2f}'.format(pm))
    print('Emprestímo NEGADO!')
else:
    print('Salário: R${:.2f}'.format(sc))
    print('Prestação: R${:.2f}'.format(pm))
    print('Emprestímo ACEITO!')
