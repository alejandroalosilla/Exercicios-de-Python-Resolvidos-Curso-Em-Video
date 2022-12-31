#  Ex096 - Faça um programa que tenha uma função chamada area(), que receba
# as dimensões de um terreno retangular (largura e comprimento) e
# mostre a área do terreno.

def area(a, b):
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {(a*b):.1f}m²')


print(' Controle de Terrenos')
print(22 * '-')

la = float(input('Largura: '))
c = float(input('Comprimento: '))
area(la, c)
