# Escreva um algoritmo que 
# leia o código de um determinado produto e 
# mostre a sua classificação. Utilize a seguinte tabela como referência:
# Codigo            Referencia
# 1                 Alimento não-perecível 
# 2, 3 ou 4         Alimento perecível
# 5 ou 6            Vestuário
# 7                 Higiene pessoal
# 8 até 15          Limpeza e utensílios domésticos
# Qualquer outro    Inválido

codigo = int(input('Informe o código do produto: '))

if codigo == 1 :
    print('É um alimento não-perecível.')

if codigo == 2 or codigo == 3 or codigo == 4 : 
    print('É um alimento perecível.')

if codigo == 5 or codigo == 6 : 
    print('É um produto de vestuário.')

if codigo == 7 : 
    print('É um produto de higiene pessoal.')

if 7 < codigo < 16 : 
    print('É um produto de limpeza/utensílios domésticos.')

if codigo == 0 or codigo > 15 :
    print('Inválido')

print('=)')