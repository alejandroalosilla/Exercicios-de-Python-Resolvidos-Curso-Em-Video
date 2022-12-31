#  Ex113 - Reescreeva a função leiaint() que fizemos no desafio 104, incluindo
# agora a possibilidade da digitação de um número de tipo inválido.
#  Aproveite e crie também uma função leiafloat() com a mesma
# funcionalidade.

def leiaint(i1):
    while True:
        try:
            a = int(input(i1))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número!\033[m')
            a = 0
            return a
        except ValueError:
            print('\033[31mERRO: por favor, digite um número inteiro válido!\033[m')
        else:
            return a


def leiafloat(f1):
    while True:
        try:
            b = float(input(f1))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número!\033[m')
            b = 0
            return b
        except ValueError:
            print('\033[31mERRO: por favor, digite um número real válido!\033[m')
        else:
            return b


i = leiaint('Digite um inteiro: ')
f = leiafloat('Digite um real: ')
print(f'O valor inteiro digitado foi {i} e o real {f} foi ')
