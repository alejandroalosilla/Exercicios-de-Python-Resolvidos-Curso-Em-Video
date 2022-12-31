#  Ex103 - Faça um programa que tenha uma função chamada ficha(), que receba
# dois parâmetros opcionais: o nome de um jogador e quantos gols ele
# marcou.
#  O programa deverá conseguir mostrar a ficha do jogador, mesmo
# que algum dado não tenha sido informado corretamente.

def ficha(a, b):
    if a in '':
        a = '<desconhecido>'
    if b in '':
        b = 0
    print(f'O jogador {a} fez {b} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: ')).strip().capitalize()
n_gols = str(input('Número de Gols: '))
ficha(nome, n_gols)
