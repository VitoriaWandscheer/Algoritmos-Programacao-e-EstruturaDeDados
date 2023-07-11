# Um comerciante calcula o valor da venda,
# tendo em vista a tabela a seguir,
# construa um algoritmo que leia o valor da compra
# e informe ao comerciante qual o lucro obtido sobre aquela compra.
#
#          CONDIÇÃO:               LUCRO:
#   venda   <   10                  70%
#   10      <=  venda   <   30      50%
#   30      <=  venda   <   50      40%
#   v       >=  50                  30%

valor_compra = float(input('Informe o valor da compra: '))

VALOR_A = 10 # Lucro de 70% quando menor que 10 reais
VALOR_B = 30 # Lucro de 50% quando maior ou igual a 10 reais e menor que 30 reais.
VALOR_C = 50 # Lucro de 40% quando maior ou igual a 30 reais e menor que 50 reais.

SETE = 0.7
CINQ = 0.5
QUAR = 0.4
TRIN = 0.3

if valor_compra < VALOR_A :
    print(F'O lucro obtido sobre a compra foi de R${valor_compra * SETE :.2f}')

if valor_compra >= VALOR_A and valor_compra < VALOR_B :
    print(F'O lucro obtido sobre a compra foi de R${valor_compra * CINQ :.2f}')

if valor_compra >= VALOR_B and valor_compra < VALOR_C :
    print(F'O lucro obtido sobre a compra foi de R${valor_compra * QUAR :.2f}')

if valor_compra >= VALOR_C : 
    print(F'O lucro obtido sobre a compra foi de R${valor_compra * TRIN :.2f}')

print('=)')