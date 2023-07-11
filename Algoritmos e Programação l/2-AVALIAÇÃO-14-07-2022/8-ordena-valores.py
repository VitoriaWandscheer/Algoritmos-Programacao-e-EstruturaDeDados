    # QUESTÃO 08 (Valores em ordem crescente e decrescente)

i = int(input('Digite 1 para ver os valores em ordem crescente e 2 para ver o valores em ordem decrescente: \n->  '))
if i != 2 and i != 1:
    print('Digite um número válido!')
else:
    print('Digite o valor de:')
    a = float(input('a) '))
    b = float(input('b) '))
    c = float(input('c) '))

    if i == 1:
        print('\n\n\nORDEM CRESCENTE: ')
        if a < b and a < c and b < c:
            print(f'{a}, {b}, {c}')
        elif a < c and a < b and c < b:
            print(f'{a}, {c}, {b}')
        elif b < a and b < c and a < c:
            print(f'{b}, {a}, {c}')
        elif b < c and b < a and c < a:
            print(f'{b}, {c}, {a}')
        elif c < a and c < b and a < b:
            print(f'{c}, {a}, {b}')
        elif c < b and c < a and b < a:
            print(f'{c}, {b}, {a}')
    
    elif i == 2:
        print('ORDEM DECRESCENTE: ')
        if a < b and a < c and b < c:
            print(f'{c}, {b}, {a}')
        elif a < c and a < b and c < b:
            print(f'{b}, {c}, {a}')
        elif b < a and b < c and a < c:
            print(f'{c}, {a}, {b}')
        elif b < c and b < a and c < a:
            print(f'{a}, {c}, {b}')
        elif c < a and c < b and a < b:
            print(f'{b}, {a}, {c}')
        elif c < b and c < a and b < a:
            print(f'{a}, {b}, {c}')

    print('\n\n\n=)')