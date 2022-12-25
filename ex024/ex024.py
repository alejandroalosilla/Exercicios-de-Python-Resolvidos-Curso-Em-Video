#  Ex024 - Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO".

nc = str(input('Digite o nome de uma cidade: ')).strip().upper()

print('O nome da cidade começa com santo? {}'.format('SANTO' in nc))
