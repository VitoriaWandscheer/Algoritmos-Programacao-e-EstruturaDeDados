# Escreva uma função que receba a base e a altura de um triângulo e retorne a sua área (A = (base x altura)/2).

def area(x,y):
    return (x * y) / 2

x = int(input('Informe a base do triangulo: '))
y = int(input('Informe a altura do triangulo: '))

print(f'\nA área do triângulo é {area(x,y)}')

print('\n=)')