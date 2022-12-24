#  Ex004 - Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.

# cores
az = '\033[36m'
a = '\033[33m'
v = '\033[32m'
f = '\033[m'

x = input('{}Digite algo:{} '.format(az, f))

print('{}{}{} é número? {}'.format(a, x, f, x.isnumeric()))
print('{}{}{} é alfanumérico? {}'.format(a, x, f, x.isalnum()))
print('{}{}{} é letra? {}'.format(a, x, f, x.isalpha()))
print('{}{}{} está em minúsculo? {}'.format(a, x, f, x.islower()))
print('{}{}{} é decimal? {}'.format(a, x, f, x.isdecimal()))
print('{}{}{} é espaço? {}'.format(a, x, f, x.isspace()))
print('{}{}{} está em maiúsculo? {}'.format(a, x, f, x.isupper()))
