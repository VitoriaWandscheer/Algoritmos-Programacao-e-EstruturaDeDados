# Criar um algoritmo que imprima todos os números de 1 até 10,
# e a média geral de todos eles (intervalo fechado)
num = 0
soma = 0
NUM_MAX = 10

while num < NUM_MAX:
    num += 1
    print(num)
    soma = soma + num
media_geral = soma / NUM_MAX
print(f'A media geral é igual a {media_geral}')

print('=)')