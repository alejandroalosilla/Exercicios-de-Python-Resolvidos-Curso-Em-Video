#  Ex105 - Faça um programa que tenha uma função chamada notas() que pode
# receber várias notas de alunos e vai retornar um dicionário com as
# seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#  Adicione também as docstrings da função.

d = dict()


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    d['Total'] = len(n)
    d['Maior'] = max(n)
    d['Menor'] = min(n)
    d['Média'] = sum(n) / len(n)
    if sit is True:
        if d['Média'] >= 7:
            d['Situação'] = 'BOA'
        elif 6 <= d['Média'] < 7:
            d['Situação'] = 'RAZOÁVEL'
        else:
            d['Situação'] = 'RUIM'
    print(d)


print(75 * '-')
notas(6, 6, sit=True)
print()
help(notas)
