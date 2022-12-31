#  Ex102 - Crie um programa que tenha um função fatorial() que receba
# dois parâmetros: o primeiro que indique o número a calcular e o
# outro chamado show, que será um valor lógico(opcional) indicando
# se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(n, show=False):
    f = n
    for c in range(n - 1, 0, -1):
        f *= c
    if show is False:
        return f
    else:
        for c in range(n, 0, -1):
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
        return f


print(30 * '-')
print(fatorial(5, True))
