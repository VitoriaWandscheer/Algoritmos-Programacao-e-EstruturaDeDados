# Faça um programa que receba o salário base de um funcionário,
# calcule e mostre o salário a receber,
# sabendo-se que:
#   O funcionário tem gratificação de 5% sobre o salário base
#   Paga 7% de imposto também sobre o salário base

salario = float(input('Digite o salário base: '))

GRAT = 5
IMP = 7

grat = (salario * GRAT) / 100
imposto = (salario * IMP) / 100
receber = salario + grat - imposto

print (f'O salario a receber é R${receber:.2f}')

print('=)')