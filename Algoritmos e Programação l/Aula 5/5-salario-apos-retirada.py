# João recebeu seu salário e precisa pagar duas contas atrasadas.
# Em razão do atraso, ele deverá pagar multa de 2% sobre cada conta.
# Faça um programa que lê o valor do salário, das duas contas e
# calcule e mostre quanto restará do salário de João.

salario = float(input('Informe seu salario: '))
conta_a = float(input('Informe o valor da primeira conta: '))
conta_b = float(input('Informe o valor da segunda conta: '))
MULTA = 0.02

valor_com_multa = salario - ((conta_a + (conta_a * MULTA)) + (conta_b + (conta_b * MULTA)))

print(f'Após pagar suas contas restará R${valor_com_multa:.2f}.')

print('=)')