# Crie uma sub-rotina que receba como parâmetro uma lista V contendo 25 elementos de números inteiros e substitua todos os valores negativos de V por 0. A lista deverá ser retornada para quem realizou a chamada desta função.

###################################################
############## PROCEDIMENTO #######################
###################################################

def substituicao(V):
    for x in range(0, len(V)):
        if V[x] < 0:
            V[x] = 0

###################################################
##################  INPUT #########################
###################################################

V = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print('Informe os valores para V:')
for x in range(0,25):
    V[x] = int(input('= '))

###################################################
##################  PRINT #########################
###################################################

print()
print(substituicao(V))
print()
print('=)')