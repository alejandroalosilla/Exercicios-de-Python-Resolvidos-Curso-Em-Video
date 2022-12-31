#  Ex072 - Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
#  Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso.


c = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número [0-20]: '))

    if n < 0 or n > 20:
        print('Tente novamente. ', end='')
    else:
        break
print(f'Você digitou o número {c[n]}')
