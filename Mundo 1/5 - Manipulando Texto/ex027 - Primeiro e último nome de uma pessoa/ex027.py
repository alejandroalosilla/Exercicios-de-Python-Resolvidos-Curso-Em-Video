#  Ex027 - Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# EX: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

n = str(input('Digite um nome completo: ')).strip().split()

print('Primeiro nome: {}'.format(n[0]))
print('Último nome: {}'.format(n[len(n) - 1]))
