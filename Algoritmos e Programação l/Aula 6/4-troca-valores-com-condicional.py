#Faça um algoritmo que lê valores para duas variáveis X e Y. 
# Se o valor correspondente a 
# 30% da soma de x por y for maior que 500 trocar os valores entre X e Y,
# senão mostrar o menor valor entre as duas variáveis.

x = int(input('Informe um valor: '))
y = int(input('Informe outro valor: '))

PC = 0.3
NUM = 500

soma = x + y
porcent = soma * PC

if (porcent > NUM):
    a = x
    x = y
    y = a
    print (f'O valor de x é igual a {x} e o valor de y é igual a {y} ')
else:
    if (x < y): 
        print(f'O menor valor entre {x} e {y} é {x}')
    else:
        print(f'O menor valor entre {x} e {y} é {y}')

print('=)')