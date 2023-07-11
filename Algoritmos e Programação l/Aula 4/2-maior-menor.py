# Faça um programa que leia três valores inteiros fornecidos
# pelo usuário e exiba o maior e o menor dos valores lidos.
# Supor que não sejam iguais

a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceiro valor: '))

if (a > b) and (a > c) and (b < c) : # a maior e b menor
    print (f'O maior valor é {a} e o menor valor é {b}')

if (a > c) and (a>b) and (c < b) : # a maior e c menor
    print (f'O maior valor é {a} e o menor valor é {c}')

if (b > a) and (b > c) and (a < c) : # b maior e a a menor
    print (f'O maior valor é {b} e o menor valor é {a}')

if (b > c) and (b > a) and (c < a) : # b maior e c a menor
    print (f'O maior valor é {b} e o menor valor é {c}')

if (c > b) and (c > a) and (b < a) : # c maior e b a menor
    print (f'O maior valor é {c} e o menor valor é {b}')

if (c > a) and (c > b) and (a < b) : # c maior e a a menor
    print (f'O maior valor é {c} e o menor valor é {a}')

print('=)')