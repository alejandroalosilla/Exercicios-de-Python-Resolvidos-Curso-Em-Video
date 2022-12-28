#  Ex046 - Faça um programa que mostre na tela uma contagem regressiva para o estouro
# de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from emoji import emojize
from time import sleep

for c in range(10, 0, -1):
    print('\033[31m{}...\033[m'.format(c))
    sleep(1)
print(emojize('\033[36m:call_me_hand:\033[32mFeliz ano novo!\033[33m:sparkles::sparkles::sparkles:'))
