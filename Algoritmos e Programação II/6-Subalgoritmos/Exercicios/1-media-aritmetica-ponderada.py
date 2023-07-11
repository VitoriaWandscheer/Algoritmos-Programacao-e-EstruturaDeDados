# Elabore um algoritmo que receba as 3 notas de um aluno e uma letra. Se a letra for “A”, deve-se chamar uma sub-rotina que deverá calcular a média aritmética das notas dos alunos; Se a letra for “P”, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média calculada deverá ser devolvida ao programa principal para, então, ser mostrada.

###################################################
################## FUNÇÃO #########################
###################################################

nota = []

def aritmetica(nota):
    media = (nota[0]+nota[1]+nota[2]) / 3
    return media

def ponderada(nota):
    media = ((nota[0]*5) + (nota[1]*3) + (nota[2]*2)) / 10 
    return media

###################################################
################## INPUT  #########################
###################################################

print('Informe as notas do aluno:')
for x in range(0,3):
    aux = float(input('= '))
    nota.append(aux)

media = input('Informe [A] para ver a média aritmetica ou [P] para ver a média ponderada:\n= ')

###################################################
##################  PRINT #########################
###################################################

if media == 'a' or media == 'A':
    print()
    print('A média aritmética do aluno é', aritmetica(nota))
elif media == 'p' or media == 'P':
    print()
    print('A média ponderada do aluno é', ponderada(nota))
else:
    print()
    print('### erro ao informar o valor para o tipo de media ###')

print('\n=)')