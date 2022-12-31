#  Ex039 - Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo de alistamento.
#  Seu programa também deverá mostrar o tempo que falta ou
# que passou do prazo.

import datetime

aa = datetime.datetime.now()
aa = aa.year

an = int(input('Digite o ano de nascimento: '))

if (aa - an) < 18:
    print('Vai se alistar daqui a {} ano(s)!'.format(18 - (aa - an)))
elif (aa - an) == 18:
    print('É hora de se alistar!')
else:
    print('Já passou {} ano(s) do alistamento!'.format((aa - an) - 18))
