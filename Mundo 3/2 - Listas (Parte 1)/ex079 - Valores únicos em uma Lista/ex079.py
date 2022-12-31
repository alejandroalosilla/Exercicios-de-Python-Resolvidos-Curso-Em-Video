#  Ex079 - Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista.
#  Caso o número já exista lá dentro, ele não será adicionado.
#  No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

ll = list()

while True:
    v = int(input('Digite um  valor: '))

    if v in ll:
        print('Valor duplicado! Não vou adicionar...')
    else:
        ll.append(v)
        print('Valor adicionado com sucesso...')

    op = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

    if op == 'N':
        break
print(30 * '-=')
print(f'Você digitou os valores {sorted(ll)}')
