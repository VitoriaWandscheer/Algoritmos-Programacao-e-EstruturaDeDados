# Um trabalhador recebeu seu salário e o depositou em sua conta bancária.
# Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual.
# Sabe-se que cada operação bancária de retirada paga CPMF de 0,38%
# e o saldo inicial da conta está zerado.

salario = float(input('Digite o valor do seu salário: '))
cheque1 = float(input('Digite o valor do primeiro cheque: '))
cheque2 = float(input('Digite o valor do segundo cheque: '))

CPMF = 0.38/100

saldo = salario - (cheque1 + (cheque1 * CPMF))
saldo = saldo - (cheque2 + (cheque2 * CPMF))

print (f'Seu saldo atual é de R${saldo:.2f}')

print('=)')