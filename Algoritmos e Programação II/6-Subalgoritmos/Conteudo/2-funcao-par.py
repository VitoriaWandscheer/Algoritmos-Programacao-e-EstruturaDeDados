# Escreva uma função que receba um número e retorne TRUE se o número for par.

def par(x):
    if x % 2 == 0:
        return "TRUE"

x = int(input('Informe o valor que deseja verificar: '))

print(par(x))

print('\n=)')