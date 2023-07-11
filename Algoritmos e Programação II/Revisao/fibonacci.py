#   Faça um programa que receba um valor inteiro fornecido pelo usuário
#   e imprima a sequência de Fibonacci até este número.
#       "A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ..." 

valor = int(input('Informe um valor: '))
var1 = 0
var2 = 1
tot = 0
print(1)
while tot < valor:
    tot = var1 + var2
    var1 = var2
    var2 = tot
    if tot <= valor:
        print(tot)

print('=)')