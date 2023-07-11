# Criar um algoritmo que imprima todos os números de 1 até 100,
# e a soma de todos eles (intervalo fechado). 
soma = 0

for qtd in range(1, 101, 1):
    print(qtd)
    soma = soma + qtd

print(soma)

print('=)')