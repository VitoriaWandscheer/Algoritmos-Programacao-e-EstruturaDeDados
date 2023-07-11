# Faça um algoritmo que lê valores para 5 variáveis A, B, C, D e E.
# Encontrar e mostrar o maior valor digitado.

print('Informe cinco valores: ')

a = int(input('='))
b = int(input('='))
c = int(input('='))
d = int(input('='))
e = int(input('='))

if (a > b) and (a > c) and (a > d) and (a > e):
                print (f'O maior valor entre os valores {a}, {b}, {c}, {d} e {e} é {a}.')
elif (b > c) and (b > d) and (b > e):
            print (f'O maior valor entre os valores {a}, {b}, {c}, {d} e {e} é {b}.')
elif (c > d) and (c > e):
        print (f'O maior valor entre os valores {a}, {b}, {c}, {d} e {e} é {c}.')
elif (d > e):
    print (f'O maior valor entre os valores {a}, {b}, {c}, {d} e {e} é {d}.')
else:
    print (f'O maior valor entre os valores {a}, {b}, {c}, {d} e {e} é {e}.')

print('=)')