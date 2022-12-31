#  Ex093 - Crie um programa que gerencie o aproveitamento de um jogador
# de futebol.
#  O programa vai ler o nome do jogador e quantas partidas ele jogou.
#  Depois vai ler a quantidade de gols feitos em cada partida.
#  No final, tudo isso será guardado em um dicionário, incluindo o
# total de gols feitos durante o campeonato.
lg = list()
d = dict()

d['Nome'] = str(input('Nome do Jogador: ')).strip().capitalize()

tp = int(input(f"Quantas partidas {d['Nome']} jogou? "))
tg = 0
for c in range(0, tp):
    g = int(input(f'Quantos gols na partida {c}? '))
    lg.append(g)
    tg += g

d['Gols'] = lg.copy()
d['Total'] = tg
print(30 * '-=')
print(d)
print(30 * '-=')
for k, v in d.items():
    print(f'O campo {k} tem o valor {v}')
print(30 * '-=')
print(f"O jogador {d['Nome']} jogou {tp} partidas")
for pos, v in enumerate(lg):
    print(f'    => Na partida {pos}, fez {v} gols')
print(f"Foi um total de {d['Total']} gols")
