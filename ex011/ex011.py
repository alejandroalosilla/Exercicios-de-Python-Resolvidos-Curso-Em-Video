#  Ex011 - Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta,
# pinta uma área de 2m².

la = float(input('Digite a largura em metros: '))
a = float(input('Digite a altura em metros: '))
ar = la * a
qt = a / 2

print('Com a largura de {:.2f}m e a altura de {:.2f}m temos uma área de {:.2f}m²'.format(la, a, ar))
print('Precisa-se de {:.2f}l para pintar {:.2f}m²!!!'.format(la, ar))
