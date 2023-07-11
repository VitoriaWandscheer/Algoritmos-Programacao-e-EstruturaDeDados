# Criar um algoritmo que imprima todos os números de 1 até 100,
# e a soma de todos eles (intervalo fechado). 
num_inteiro = 0
soma = 0

while num_inteiro < 100:
    num_inteiro += 1
    print(num_inteiro)
    soma = soma + num_inteiro
    print(f'A soma de todos os númeoros, até agora, é igual a {soma}')

print('=)')