# Escreva um algoritmo que
# leia 20 números
# e imprima a soma dos positivos
# e o total de números negativos. 

cont = 0
soma_positivo = 0
cont_negativo = 0

while cont < 20:
    a = int(input('Informe um numero:\n'))
    if a > 0 :
        soma_positivo  = soma_positivo  + a #ACUMULADOR
    else:
        cont_negativo = cont_negativo + 1 #CONTADOR
    cont += 1 #CONTADOR

print(f'A soma dos números positivos é igual a {soma_positivo } e há {cont_negativo} número(s) negativo(s).')

print('=)')