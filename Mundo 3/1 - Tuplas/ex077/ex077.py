#  Ex077 - Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos).
#  Depois disso, você deve mostrar, para cada palavra, quais
# são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')

for p in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[p].upper()} temos ', end='')
    x = palavras[p]

    for c in range(0, len(x)):
        if x[c] in 'aeiou':
            print(x[c], end=' ')
