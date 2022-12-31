#  Ex106 - Faça um mini-sistema que utilize o interactive help do Python.
#  O usuário vai digitar o comando e o manual vai aparecer.
#  Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# OBS: use cores

from time import sleep


def p(msg, c):
    print((len(msg) + 4) * f'\033[;{c}m~')
    print(f'  {msg}')
    print((len(msg) + 4) * '~', end='\n\033[m')


while True:
    p('SISTEMA DE AJUDA PyHELP', 42)
    op = str(input('Função ou Biblioteca > ')).strip().lower()
    if op == 'fim':
        p('ATÉ LOGO!', 41)
        break
    p(f"Acessando o manual do comando '{op}'", 44)
    sleep(2)
    print('\033[7m', end='')
    help(op)
    sleep(2)
