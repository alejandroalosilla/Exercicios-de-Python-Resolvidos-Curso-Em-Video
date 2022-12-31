def leiadinheiro(d):
    d = str(input(d)).strip()
    if d.find(',') != -1:
        d = d.replace(',', '.')
    while d.isalpha() is True or d == '':
        print(f'\033[31mERRO: "{d}" é um preço inválido!\033[m')
        d = str(input('Digite o preço: R$')).strip()
    return float(d)
