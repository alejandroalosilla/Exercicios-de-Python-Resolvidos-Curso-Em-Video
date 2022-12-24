# Ex003 - Crie um script Python que leia dois números e tente
# mostrar a soma entre eles.

#  cores
azul = '\033[36m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
fechar = '\033[m'

print(20 * '{}={}'.format(azul, fechar))
n1 = int(input('{}Primeiro número: '.format(amarelo)))
n2 = int(input('{}Segundo número: '.format(amarelo)))
print(20 * '{}={}'.format(azul, fechar))

s = n1 + n2
print('{}A soma entre {}{}{} {}e {}{}{} {}é {}{}{}{}!'.format(amarelo, vermelho, n1, fechar, amarelo, vermelho, n2,
                                                              fechar, amarelo, verde, s, fechar, amarelo))
