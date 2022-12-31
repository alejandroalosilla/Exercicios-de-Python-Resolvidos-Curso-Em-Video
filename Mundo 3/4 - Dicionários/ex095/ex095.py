#  Ex095 - Aprimore o DESAFIO 093 para que ele funcione com vários
# jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

lj = list()
d = dict()
gp = list()
tg = 0

while True:
    d['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    np = int(input(f"Quntas partidas {d['Nome']} jogou? "))
    for c in range(0, np):
        g = int(input(f'Quantos gols na partida {c}? '))
        tg += g
        gp.append(g)
    d['Gols'] = gp.copy()
    d['Total'] = tg
    lj.append(d.copy())
    d.clear()
    gp.clear()
    tg = 0

    option = ''
    while option != 'N' and option != 'S':
        option = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if option == 'N':
        break
print(30 * '-=')
print('cod Nome           Gols           Total')
print(44 * '-')
for k, v in enumerate(lj):
    print(f'{k:>3} ', end='')
    for d in lj[k].values():
        print(f'{str(d):<15}', end='')
    print()
print(44 * '-')


while True:
    j = int(input('Mostrar dados de qual jogador? '))
    if j == 999:
        break
    else:
        if j < len(lj) or j == 0:
            print(f"-- Levantamento do jogador {lj[j]['Nome']}:")
            for pos, v in enumerate(lj[j]['Gols']):
                print(f'   No jogo {pos} fez {v} gols.')
        else:
            print(f'ERRO! Não existe jogador com código {j}! Tente novamente')
            print(44 * '-')

print('<< VOLTE SEMPRE >>')
