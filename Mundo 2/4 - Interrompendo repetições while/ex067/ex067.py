#  Ex067 - Faça um programa que mostre a tabuada de vários
# números, um de cada vez, para cada valor digitado
# pelo usuário.
#  O programa será interrompido quando o número soli-
# citado for negativo.

while True:
    n = int(input('Quer ver a tabuada de qual número: '))
    print(20 * '-')
    if n < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{n} x {c} = {n * c}')
            c += 1
    print(20 * '-')
print('Programa tabuada encerrado. Volte sempre!')
