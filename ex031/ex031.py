#  Ex031 - Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem,cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 para viagens
# mais longas.

dv = float(input('Digite a distância em Km: '))

if dv <= 200:
    pp = dv * 0.50
    print('Preço da passagem: R${:.2f}'.format(pp))
else:
    pp = dv * 0.45
    print('Preço da passagem: R${:.2f}'.format(pp))
