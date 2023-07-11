print('Informe três valores diferentes: ')

a = int(input('1º valor: '))
b = int(input('2º valor: '))
c = int(input('3º valor: '))

if (a > b) and (a > c) and (b < c) : # c intermediario - caso 1
    print (f'O valor intermediário entre os númeors {a}, {b} e {c} é {c}.')

if (a > c) and (a>b) and (c < b) : # b intermediário - caso 1
    print (f'O valor intermediário entre os númeors {a}, {b} e {c} é {b}.')

if (b > a) and (b > c) and (a < c) : # c intermediário - caso 2
    print (f'O valor intermediário entre os númeors {a}, {b} e {c} é {c}.')

if (b > c) and (b > a) and (c < a) : # a intermediário - caso 1
    print (f'O valor intermediário entre os númeors {a}, {b} e {c} é {a}.')

if (c > b) and (c > a) and (b < a) : # a intermediário -  caso 2
    print (f'O valor intermediário entre os númeors {a}, {b} e {c} é {a}.')

if (c > a) and (c > b) and (a < b) : # b intermediário - caso 2
    print (f'O valor intermediário entre os númeors {a}, {b} e {c} é {b}.')

print('=)')