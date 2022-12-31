#  Ex049 - Refaça o DESAFIO 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando laço for.

n = int(input('Digite um número inteiro: '))
print(20 * '=')
print('Tabuada do {}!'.format(n))
print(20 * '=')
for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, n * c))
print(20 * '=')
