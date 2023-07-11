# Escreva uma função que receba o lado de um quadrado e retorne a sua área (A = lado2).

def area(x):
    return x ** 2

x = int(input('Informe o lado do quadrado: '))

y = area(x)

print(f'A área do quadrado de lado {x} é {y}.')

print('\n=)')