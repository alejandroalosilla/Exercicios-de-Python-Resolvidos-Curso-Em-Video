#  Ex006 - Crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um número: '))

d = n * 2
t = n * 3
rq = pow(n, 1/2)

print('Dobro de {}: {}\nTriplo de {}: {}\nRaíz Quadrada de {}: {} '.format(n, d, n, t, n, rq))
