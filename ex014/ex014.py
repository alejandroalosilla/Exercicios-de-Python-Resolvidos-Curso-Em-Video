#  Escreva um programa que converta uma temperatura digitando
# em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite uma temperatura em graus Celsius: '))
f = (1.8 * c) + 32

print('A conversão de {}ºC é: {}ºF'.format(c, f))
