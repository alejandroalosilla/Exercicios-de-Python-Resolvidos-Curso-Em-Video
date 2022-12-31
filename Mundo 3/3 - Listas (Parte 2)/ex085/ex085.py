#  Ex085 - Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores
# pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.

ll = list()
dado_p = list()
dado_i = list()

for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º valor: '))
    if n % 2 == 0:
        dado_p.append(n)
    else:
        dado_i.append(n)

ll.append(dado_p[:])
ll.append(dado_i[:])

print(30 * '-=')
print(f'Os valores PARES digitados foram: {sorted(ll[0])}')
print(f'Os valores ÍMPARES digitados foram: {sorted(ll[1])}')
