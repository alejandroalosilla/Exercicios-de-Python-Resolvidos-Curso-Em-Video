#  Ex092 - Crie um programa que leia nome, ano de nascimento e carteira
# de trabalho e cadastre-os (com idade) em um dicionário se por
# acaso a CTPS for diferente de ZERO, o dicionário receberá também
# o ano de contratação e o salário.
#  Calcule e acrescente, além da idade, com quantos anos a pessoa
# vai se aposentar.

from datetime import datetime
aa = datetime.now().year

d = dict()

d['Nome'] = str(input('Nome: ')).strip().capitalize()
d['Idade'] = aa - int(input('Ano de nascimento: '))
print(30 * '-=')
d['CTPS'] = int(input('Carteira de Trabalho (0 não  tem): '))
if d['CTPS'] != 0:
    d['Contratação'] = int(input('Ano de contratação: '))
    d['Salário'] = float(input('Salário: R$'))
    d['Aposentadoria'] = (d['Idade'] + 35) - (aa - d['Contratação'])

for k, v in d.items():
    print(f'{k} tem o valor {v}')
