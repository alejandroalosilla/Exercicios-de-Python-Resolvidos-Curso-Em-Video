#  Ex037 - Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de coversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

n = int(input('Digite um número inteiro qualquer: '))
print(20 * '=')
print('Selecione a base de conversão:')
print('[1] para binário')
print('[2] para octal')
print('[3] para hexadecimal')
e = int(input('=> '))
print(20 * '=')

if e == 1:
    print('Conversão do número {} para binário: {}'.format(n, bin(n)))
elif e == 2:
    print('Conversão do número {} para octal: {}'.format(n, oct(n)))
elif e == 3:
    print('Conversão do número {} para hexadecimal: {}'.format(n, hex(n)))
else:
    print('\033[31mOpção errada!!!\033[m')
