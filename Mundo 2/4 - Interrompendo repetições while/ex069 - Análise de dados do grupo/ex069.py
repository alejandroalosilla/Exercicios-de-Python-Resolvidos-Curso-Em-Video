#  Ex069 - Crie um programa que leia a idade e o sexo de várias pessoas.
#  A cada pessoa cadastrada, o programa deverá perguntar se o
# usuário quer ou não continuar.
#  No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 10 anos.

md = 0
th = 0
mv = 0

while True:
    print(20 * '-')
    print('CADASTRE UMA PESSOA')
    print(20 * '-')
    i = int(input('Idade: '))
    while True:
        s = str(input('Sexo [M/F]: ')).strip().upper()
        if s == 'M' or s == 'F':
            break

    if i > 18:
        md += 1
    if s == 'M':
        th += 1
    if s == 'F' and i < 20:
        mv += 1

    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if r == 'S' or r == 'N':
            break
    if r == 'N':
        break
print('==== FIM DO PROGRAMA ====')
print(f'Total de pessoas com mais de 18 anos: {md}')
print(f'Ao todo temos {th} homens cadastrados')
print(f'E temos {mv} mulheres com menos de 20 anos')
