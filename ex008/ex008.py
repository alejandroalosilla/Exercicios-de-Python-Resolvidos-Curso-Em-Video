#  Ex008 - Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros

m = float(input('Digite um valor em metros: '))
cm = m * 100
mm = m * 1000

print('{:.2f}m são {:.2f}cm'.format(m, cm))
print('{:.2f}m são {:.2f}mm'.format(m, mm))
