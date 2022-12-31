# Ex057 - Faça um programa que leia o sexo de uma pessoa, mas
# só aceite os valores 'M' ou 'F'.
#  Caso esteja errado, peça a digitação novamente
# até ter um valor correto.

r = ''

while r != 'M' and r != 'F':
    r = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()
    if r != 'M' and r != 'F':
        print('O valor {} está incorreto! Digite novamente! '.format(r))
if r == 'M':
    print('O sexo é MASCULINO!')
elif r == 'F':
    print('O sexo é FEMININO!')
