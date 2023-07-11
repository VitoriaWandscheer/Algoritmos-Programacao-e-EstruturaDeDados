# Faça um algoritmo que lê 10 valores para uma variável do tipo vetor
# e mostre qual a posição está armazenado o maior e o menor valor no vetor.

import numpy as np

N = 5
vetor = np.zeros(N)

print('Informe um valor para a posição:')
for i in range(0, N):
    vetor[i] = float(input(f'[{i}]: '))

maior = vetor[0]
menor = vetor[0]

menor_indice = 0
maior_indice = 0

for i in range(0, N):
    if maior < vetor[i]:
        maior = vetor[i]
        maior_indice = i
    if menor > vetor[i]:
        menor = vetor[i]
        menor_indice = i

print(f'O maior valor é {maior} e está na posição [{maior_indice}].')
print(f'O menor valor é {menor} e está na posição [{menor_indice}].')


print('=)')