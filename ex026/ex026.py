#  Ex026 - Faça um programa que leia uma frase pelo teclado
# e mostre:
# -> Quantas vezes aparece a letra "A".
# -> Em que posição ela aparece a primeira vez.
# -> Em que posição ela aparece a última vez.

f = str(input('Digite uma frase: ')).strip().upper()

print('Quantas vezes aparece a letra "A"? {}'.format(f.count('A')))
print('Aparece pela primeira vez na posição: {}'.format(f.find('A')))
print('Aparece a última vez na posição: {}'.format(f.rfind('A')))
