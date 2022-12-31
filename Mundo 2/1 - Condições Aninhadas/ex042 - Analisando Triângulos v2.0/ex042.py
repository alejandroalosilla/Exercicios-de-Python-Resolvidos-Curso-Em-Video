#  Ex042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

a = float(input('Comprimento a: '))
b = float(input('Comprimento b: '))
c = float(input('Comprimento c: '))

if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    print('\033[32mAs medidas formam um triângulo!\033[m')
    if a == b and a == c:
        print('TRIÂNGULO EQUILÁTERO!')
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print('TRIÂNGULO ISÓSCELES!')
    elif a != b and a != c and b != c:
        print('TRIÂNGULO ESCALENO!')
else:
    print('\033[31mAs medidas não formam um triângulo!\033[m')
