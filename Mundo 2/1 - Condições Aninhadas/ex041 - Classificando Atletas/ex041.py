#  Ex041 - A confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

import datetime

aa = datetime.datetime.now()
aa = aa.year

an = int(input('Digite o ano de nascimento do atleta: '))
i = aa - an

if i <= 9:
    print('Categoria MIRIM!')
elif 9 < i <= 14:
    print('Categoria INFANTIL!')
elif 14 < i <= 19:
    print('Categoria JUNIOR!')
elif 19 < i <= 20:
    print('Categoria SÊNIOR!')
elif i > 20:
    print('Categoria MASTER!')
