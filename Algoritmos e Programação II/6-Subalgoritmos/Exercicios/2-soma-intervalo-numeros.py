# Faça um algoritmo contendo uma sub-rotina que receba dois números positivos inteiros por parâmetro
# e retorne a soma dos N números inteiros existentes entre eles, incluindo na soma os dois números informados.

###################################################
################## FUNÇÃO #########################
###################################################

def soma_x(x,y):
    soma = x
    while x > y:
        soma = soma + (x-1)
        x = x-1
    return soma

def soma_y(x,y):
    soma = y
    while y > x:
        soma = soma + (y-1)
        y = y-1
    return soma

###################################################
##################  INPUT #########################
###################################################

print('Informe dois valores:')
x = int(input('= '))
y = int(input('= '))

###################################################
##################  PRINT #########################
###################################################

if (x<0) or (y<0):
    print()
    print('O valor informado foi negativo. Por favor digite apenas números positivos.')    
elif (x > y):
    print()
    print(f'A soma do intervalo [ {x} >>>> {y} ] é igual a:')
    print(soma_x(x,y))
else:
    print()
    print(f'A soma do intervalo [ {y} >>>> {x} ] é igual a:')
    print(soma_y(x,y))

print('\n=)')