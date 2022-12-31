def aumentar(n):
    n = n + (n * 0.1)
    return n


def diminuir(n):
    n = n - (n * 0.13)
    return n


def dobro(n):
    n = 2 * n
    return n


def metade(n):
    n = n / 2
    return n


def moeda(n):
    n = f'\033[32mR${n:.0f},00\033[m'
    return n
