# Desenvolva um gerador de tabuada (use o for), capaz de gerar a
#tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
#informar de qual número ele deseja ver a tabuada. A saída deve ser
#conforme o exemplo abaixo:
#Tabuada de 5:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50

tabuada = int(input('Informe o número que deseja saber a tabuada:\n '))

for x in range(1, 11, 1):

    print(f'{tabuada} x {x} = {tabuada * x}') 

print('=)')
