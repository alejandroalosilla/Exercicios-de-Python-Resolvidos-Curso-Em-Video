# Ex002 - Crie um script Python que leia o dia, o mês e o ano de
# nascimento de uma pessoa e mostre uma mensagem com a data
# formatada.

print(20 * '\033[35m=\033[m', end='')
print('\033[31m')
d = int(input('Dia: '))
m = str(input('Mês: '))
a = int(input('Ano: '))
print('\033[m', end='')
print(20 * '\033[35m=\033[m')

cor = {'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'fecha': '\033[m'}
print('{}Você nasceu no dia {}{}{} {}de {}{}{} {}de {}{}{}{}. Correto?'
      .format(cor['amarelo'], cor['azul'], d, cor['fecha'], cor['amarelo'], cor['azul'], m, cor['fecha'],
              cor['amarelo'], cor['azul'], a, cor['fecha'], cor['verde']))
