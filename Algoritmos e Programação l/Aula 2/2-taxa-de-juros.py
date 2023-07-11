# Faça um programa que receba o valor de um depósito e o valor da taxa de juros anual,
# calcule e mostre o valor do rendimento e o valor total depois do rendimento (após 1 ano);

val_dep = float(input('Digite o valor do depósito: '))
taxa = float(input('Digite o valor da taxa de juros anual: '))

rend = val_dep * taxa / 100
total = val_dep + rend

print (f'O valor do rendimento é de R${rend:.2f}') # variavel:.Xf = o valor da variavel será mostrado com X casas decimais.
print (f'O valor total do rendimento após um ano é de R${total}')

print('=)')