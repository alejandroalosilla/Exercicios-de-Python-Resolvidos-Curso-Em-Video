#  Ex104 - Crie um programa que tenha a função leiaint(), que vai funcionar
# de forma semelhante à função input() do Python, só que fazendo a
# validação para aceitar apenas um valor numérico.
# Ex:
# n = leiaint('Digite um n')

def leiaint(a):
    b = str(input(a))
    while b.isnumeric() is False:
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        b = str(input(a))
    return b


print(30 * '-')
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
