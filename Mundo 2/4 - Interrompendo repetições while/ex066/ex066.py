#  Ex066 - Crie um programa que leia vários números inteiros
# pelo teclado.
#  O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada.
#  No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag)

tn = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    tn += 1

print(f'Quantidade de números digitados: {tn}')
print(f'Soma dos números digitados: {s}')
