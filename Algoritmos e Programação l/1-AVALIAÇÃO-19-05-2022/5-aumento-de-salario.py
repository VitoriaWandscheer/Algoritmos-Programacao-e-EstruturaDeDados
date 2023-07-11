salario = float(input('Qual seu salário? '))

AUM_A = 0.1
AUM_B = 0.15

if salario > 1100 :
    aumento = salario * AUM_A
    print(f'Seu salário receberá um aumento de R${aumento:.2f}')
else : 
    aumento = salario * AUM_B
    print(f'Seu salário receberá um aumento de R${aumento:.2f}')

print('=)')