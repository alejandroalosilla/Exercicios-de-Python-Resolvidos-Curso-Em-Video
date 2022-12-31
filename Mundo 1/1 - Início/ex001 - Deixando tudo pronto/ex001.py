# Ex001 - Crie um script python que leia o nome de uma pessoa
# e mostre uma mensagem de boas-vindas de acordo com o
# valor digitado.

nome = str(input('Qual é o seu nome? '))
print('{}Seja bem-vindo{} {}{}!'.format('\033[33m', '\033[m', '\033[31m', nome))
