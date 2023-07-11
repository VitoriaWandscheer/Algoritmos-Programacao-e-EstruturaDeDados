# Faça um algoritmo que lê 5 valores para uma variável do tipo vetor
# e determine a média de todos valores armazenados no vetor.

import numpy as np

# Determina o tamanho da Array
N = 5

# Preenche Array com zeros
vetor = np.zeros(N)
soma = 0
print('Informe um valor para a posição ')
for i in range(0, N):
    vetor[i] = float(input(f'[{i}]: '))
    soma = soma + vetor[i]

media = soma / N

print(f'A media dos valores armazenados no vetor {vetor} é igual a {media}.')

print('=)')