# Faça um programa que leia o nome de um aluno e duas notas,
# calcule e mostre a média ponderada dessas notas,
# considerando peso 2 para a primeira nota e peso 3 para a segunda nota.

nome = str(input('Informe o nome do aluno: '))
n1 = float(input('Informe a primeira nota: ' ))
n2 = float(input('Agora informe a segunda nota: '))

PESO_N1 = 2
PESO_N2 = 3

DIV = PESO_N1 + PESO_N2

media = (n1 * PESO_N1 + n2 * PESO_N2) / DIV

print (f'A media ponderada do(a) aluno(a) {nome} é {media}.')

print('=)')