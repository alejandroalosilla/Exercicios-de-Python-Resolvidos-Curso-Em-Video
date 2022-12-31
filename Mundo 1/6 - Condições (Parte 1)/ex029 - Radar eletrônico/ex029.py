#  EX029 - Escreva um programa que leia a velocidade de um carro.
#  Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
# foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.

vc = float(input('Digite a velocidade do carro: '))

if vc > 80:
    m = (vc - 80) * 7
    print('Você foi multado por excesso de velocidade!')
    print('Valor da Multa: R${:.2f}'.format(m))
else:
    print('Boa Viagem!')
   