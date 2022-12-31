from time import sleep


def arq_existe(nome):
    try:
        n = open(nome, 'rt')
        n.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except FileNotFoundError:
        print('\033[31mHouve um ERRO na criação do arquivo!\033[m')
        sleep(3)
    else:
        print(f'\033[32mArquivo {nome} criado com sucesso!\033[m')
        sleep(3)


def ler_arq(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        print('Erro ao ler o arquivo!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        sleep(3)
        a.close()


def cadastrar(a, n='desconhecido', i=0):
    try:
        ar = open(a, 'at')
    except FileNotFoundError:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            ar.write(f'{n};{i}\n')
        except FileNotFoundError:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {n} adicionado.')
            ar.close()
