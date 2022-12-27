#  Ex025 - Crie um programa que leia o nome de uma pessoa e diga
# se ela tem 'SILVA' no nome.

n = str(input('Digite um nome: ')).strip().upper()

print('A pessoa tem "Silva" no nome? {}'.format('SILVA' in n))
