# Sabe-se que:
# 
#   1 Pé      =   12 polegadas
#   1 jarda   =   3 pés
#   1 milha   =   1.760 jardas
# 
# Faça um programa que receba uma medida em pés, faça as conversões
# e a seguir mostre os resultados em polegadas, jardas e milhas.

POLEG = 12
JARDA = 1/3
MILHA = 1/5280

pes = float(input('Digite o valor (em pés) que você deseja converter: '))

poleg = pes * POLEG
jard = pes * JARDA
mil = pes * MILHA

print (f'{pes} pés é igual a {poleg} polegadas.\n{pes} pés é igual a {jard:.2f} jardas.\n{pes} pés é igual a {mil:.6f} milhas.')

print('=)')