# Escreva uma função que receba dois números e retorne o maior.

def maior(a,b):
    if a > b:
        print(f'\nEntre os valores {a} e {b}, o maior valor é {a}.')
    else:
        print(f'\nEntre os valores {a} e {b}, o maior valor é {b}.')

a = int(input('Informe o valor de A:\n= '))
b = int(input('Informe o valor de B:\n= '))

maior(a,b)

print('\n=)')