# A granja Frangotech possui um controle automatizado de cada frango da sua produção.
# No pé direito do frango há :
# um anel com um chip de identificação.
# no pé esquerdo são:
# dois anéis para indicar o tipo de alimento que ele deve consumir.
# Sabendo que o anel com chip custa R$4,00 e o anel de alimento custa R$3,50 cada,
# faça um algoritmo para calcular o gasto total da granja para marcar todos os seus frangos.

num_frango = int(input('Informe a quantidade de frangos da granja: '))

ANEL_CHIP = 4
ANEL_ALIM = 2 * 3.5

gasto_total = (num_frango * ANEL_CHIP) + (num_frango * ANEL_ALIM)

print (f'Para marcar todos os seus franfos a granja Frangotech gastou um total de R${gasto_total:.2f}')

print('=)')