#  Ex034 - Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
#  Para salários superiores a R$1.250,00, calcule um aumento
# de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Digite o salário: '))

if s > 1250:
    s = s + (0.1 * s)
    print('O novo salário com 10% de aumento: {}'.format(s))
elif s <= 1250:
    s = s + (0.15 * s)
    print('O novo salário com 15% de aumento: {}'.format(s))
