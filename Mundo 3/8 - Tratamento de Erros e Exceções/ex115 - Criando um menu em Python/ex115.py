#  Ex115 - Vamos criar um menu em Python, usando modularização.  

from interface import *
from arquivo import *
from time import sleep

arq = 'lista.txt'

if arq_existe('lista.txt') is True:
    print('\033[32mArquivo encontrado com sucesso!\033[m')
    sleep(1)
else:
    print('\033[31mArquivo não encontrado!\033[m')
    sleep(1)
    criar_arq(arq)


while True:
    pm('              Menu Principal')
    print('\033[33m1 - \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2 - \033[34mCadastrar nova Pessoa\033[m')
    print('\033[33m3 - \033[34mSair do Sistema\033[m')
    pl()
    while True:
        while True:
            try:
                op = int(input('\033[33mSua Opção: \033[m'))
            except ValueError:
                print('\033[31mERRO: por favor, digite um número inteiro válido\033[m')
            else:
                break

        if op in [1, 2, 3]:
            break
        else:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
    if op == 1:
        pm('            PESSOAS CADASTRADAS')
        ler_arq(arq)
    if op == 2:
        pm('               NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        while True:
            try:
                idade = int(input('Idade: '))
            except ValueError:
                print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            else:
                break
        cadastrar(arq, nome, idade)
    if op == 3:
        pm('       Saindo do sistema...')
        sleep(3)
        break
print('Finalizando...')
sleep(1)
print('Até logo!')
