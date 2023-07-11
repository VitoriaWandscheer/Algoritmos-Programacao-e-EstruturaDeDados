# Escreva um algoritmo que leia
# o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina).
# Calcule e imprima o valor a ser pago pelo cliente
# sabendo-se que
# o preço do litro da gasolina é R$ 7,20
# o preço do litro do álcool é R$ 6,50.
# O posto está vendendo combustíveis com a seguinte tabela de descontos:

from json.encoder import ESCAPE


lit = float(input('Informe a quantidade de litros:\n '))
tipo = str(input('Informe o tipo de combustivel (A para álcool e G para gasolina):\n '))

PA = 6.5 # preço por litro do alcool
PG = 7.2 # preço por litro da gasosa
DESC = 20 # Parametro de litros 
D1 = 0.3 # até 20 litros (alcool), desconto de 3% por litro no valor
D2 = 0.5 # acima de 20 litros (alcool), desconto de 5% por litro no valor
D3 = 0.4 # até 20 litros (gasosa), desconto de 4% por litro no valor
D4 = 0.6 # acima de 20 litros (gasosa), desconto de 6% por litro no valor

total = PA * lit

if (tipo == 'A') or (tipo == 'a'):
    total = PA * lit
    if (lit <= DESC):
        total = total - (total * D1)
        print(f'R${total:.2f}')
    else:
        total = total - (total * D2)
        print(f'R${total:.2f}')
else:
    total = PG * lit
    if (lit <= DESC):
        total = total - (total * D3)
        print(f'R${total:.2f}')
    else:
        total = total - (total * D4)
        print(f'R${total:.2f}')

print('=)')

