#  Ex090 - Faça um programa que leia nome e média de um aluno, guardando
# também a situação em um dicionário.
#  No final, mostre o conteúdo da estrutura na tela.

nome = str(input('Nome: ')).strip().capitalize()
media = float(input(f'Média de {nome}: '))
aluno = dict()
aluno['Nome'] = nome
aluno['Média'] = media
if media >= 7:
    aluno['Situação'] = '\033[32mAprovado'
else:
    aluno['Situação'] = '\033[31mReprovado'
for k, v in aluno.items():
    print(f'\033[33m{k}\033[m é igual a \033[36m{v}')
