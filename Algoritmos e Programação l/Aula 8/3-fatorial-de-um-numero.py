# Faça um programa que calcule
# o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5! = 5.4.3.2.1 = 120 (use o for).

numero = int(input('Informe o número que deseja saber o fatorial:\n'))
x = numero

for x in range(1, numero, 1):
    numero = numero * x

print(f'{x+1}! = {numero}')

print('=)')