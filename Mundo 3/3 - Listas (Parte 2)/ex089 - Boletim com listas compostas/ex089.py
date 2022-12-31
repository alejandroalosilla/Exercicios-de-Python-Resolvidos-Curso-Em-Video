#  Ex089 - Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta.
#  No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

from time import sleep

li = list()
ln = list()

while True:
    n = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))

    ln.append(n)
    ln.append(n1)
    ln.append(n2)
    m = (n1 + n2) / 2
    ln.append(m)
    li.append(ln[:])
    ln.clear()

    op = ''
    while op != 'S' and op != 'N':
        op = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if op == 'N':
        break
print(40 * '-=')
print('No. NOME          MÉDIA')
print(30 * '-')
cont = 0
for c in range(0, len(li)):
    print(f'{c:<4}{li[c][0]:<15}{li[c][3]:.2f}')
print(30 * '-')
while True:
    na = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if na == 999:
        break
    print(f'Notas de {li[na][0]} são {li[na][1:3]}')
print('Finalizando...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')
