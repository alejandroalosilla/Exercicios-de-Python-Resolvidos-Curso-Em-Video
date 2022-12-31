#  Ex101 - Crie um programa que tenha uma função chamada voto() que vai
# receber como parâmetro o ano de nascimento de uma pessoa, retornando
# um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou
# OBRIGATÓRIO nas eleições.

from datetime import datetime
aa = datetime.now().year


def voto(a):
    i = aa - a
    if 18 <= i <= 70:
        return f'Com {i} anos: VOTO OBRIGATÓRIO.'
    elif i < 18:
        return f'Com {i} anos: NÃO VOTA.'
    else:
        return f'Com {i} anod: VOTO OPCIONAL'


print(30 * '-')
an = int(input('Em que ano você nasceu? '))
print(voto(an))
