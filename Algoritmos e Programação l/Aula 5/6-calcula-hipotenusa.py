# Faça um programa que receba o valor dos catetos de um triângulo,
# calcule e mostre o valor da hipotenusa.

cateto_a = float(input('Informe o valor do cateto adjacente: '))
cateto_o = float(input('Informe o valor do cateto oposto: '))

hipotenusa = ((cateto_a ** 2) + (cateto_o ** 2)) / 0.5

print(f'O valor da hipotenusa é {hipotenusa}.')

print('=)')