#  Ex068 - Faça um programa que jogue par ou ímpar com o computador.
#  O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele
# consquistou no final do jogo.

from random import randint

x = ''
tv = 0

print(20 * '=-')
print('VAMOS JOGAR PAR OU ÍMPAR!')
print(20 * '=-')

while True:
    pc = randint(1, 10)
    v = int(input('Digite um valor: '))
    r = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    s = pc + v
    if r == 'P' and s % 2 == 0:
        x = 'PAR'
        print(20 * '-')
        print(f'Você jogou {v} e o computador {pc}. Total de {s} DEU {x}')
        print(20 * '-')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print(20 * '=-')
        tv += 1
    elif r == 'P' and s % 2 != 0:
        x = 'ÍMPAR'
        break
    if r == 'I' and s % 2 != 0:
        x = 'ÍMPAR'
        print(20 * '-')
        print(f'Você jogou {v} e o computador {pc}. Total de {s} DEU {x}')
        print(20 * '-')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print(20 * '=-')
        tv += 1
    elif r == 'I' and s % 2 == 0:
        x = 'PAR'
        break

print(20 * '-')
print(f'Você jogou {v} e o computador {pc}. Total de {s} DEU {x}')
print(20 * '-')
print('Você PERDEU!')
print(20 * '=-')
print(f'GAME OVER! Você venceu {tv} vezes.')
