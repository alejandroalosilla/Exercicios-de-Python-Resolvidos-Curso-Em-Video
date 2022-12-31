def aumentar(n, a):
    n = n + (n * (a / 100))
    return n


def diminuir(n, d):
    n = n - (n * (d / 100))
    return n


def dobro(n):
    n = 2 * n
    return n


def metade(n):
    n = n / 2
    return n


def forma(n):
    n = f'\033[32mR${n:.0f},00\033[m'
    return n


def resumo(v, p1, p2):
    print(30 * '-')
    print('     RESUMO DO VALOR')
    print(30 * '-')
    print(f'Preço analisado:    {forma(v)}')
    print(f'Dobro do preço:     {forma(dobro(v))}')
    print(f'Metade do preço:    {forma(metade(v))}')
    print(f'{p1}% de aumento:     {forma(aumentar(v, p1))}')
    print(f'{p2}% de redução:     {forma(diminuir(v, p2))}')
    print(30 * '-')
