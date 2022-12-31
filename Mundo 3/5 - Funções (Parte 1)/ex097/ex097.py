#  Ex097 - Faça um programa que tenha uma função chamada escreva(), que receba
# um texto qualquer como parâmetro e mostre uma mensagem com tamanho
# adaptável.
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~~~~~~

def escreva(msg):
    def p():
        print((len(msg) + 4) * '~')
    p()
    print(f'  {msg}')
    p()


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
escreva('Alejandro Thierry Anry de Souza Alosilla')
