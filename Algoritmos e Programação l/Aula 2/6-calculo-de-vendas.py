# Uma padaria vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia.
# Cada pão custa R$ 0,50 e a broa custa R$ 1,50.
# Ao final do dia, o dono quer saber
# quanto arrecadou com a venda dos pães e broas (juntos),
# e quanto deve guardar numa conta de poupança (10% do total arrecadado).
# Faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados solicitados.

broas = int(input('Quantas broas foram vendidas hoje? '))
paes = int(input('Quantos pães franceses foram vendidos hoje? '))

BROA = 1.5
PAO = 0.5
GUARDAR = 0.1

venda = (broas * BROA) + (paes * PAO)
guardar = venda * GUARDAR

print (f'Hoje foram arrecados R${venda} com a venda de pães e broas.\nDevem ser guardados na conta poupança R${guardar}.')

print('=)')