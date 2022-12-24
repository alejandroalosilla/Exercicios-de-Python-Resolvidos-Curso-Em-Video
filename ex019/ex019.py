#  Ex019 - Um professor quer sortear um dos seus quatro alunos para
# apagar o quadro. Faça um programa que ajude ele, lendo
# o nome deles e escrevendo o nome do escolhido.
from random import choice

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))

li = [n1, n2, n3, n4]
e = choice(li)

print('O escolhido foi: {}'.format(e))
