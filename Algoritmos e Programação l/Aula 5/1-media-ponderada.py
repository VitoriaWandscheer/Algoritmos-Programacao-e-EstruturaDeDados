# Faça um programa que receba três notas,
# calcule e mostre a média ponderada dessas notas,
# considerando
# peso 3 para a primeira nota,
# peso 2 para a segunda nota
# e peso 5 para a terceira nota.

n1 = float(input('Informe a primera nota: '))
n2 = float(input('Informe a segunda nota: '))
n3 = float(input('Informe a terceira nota: '))

P1 = 3
P2 = 2
P3 = 5

DIV = P1 + P2 + P3

media = ((n1 * P1) + (n2 * P2) + (n3 * P3)) / DIV

print(f'A media ponderada das notas {n1}, {n2} e {n3} é {media}')

print('=)')