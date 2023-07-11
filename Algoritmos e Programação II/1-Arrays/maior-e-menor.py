# Faça um algoritmo que lê 5 valores para uma variável do tipo vetor
# e determine o maior e o menor valor armazenado no vetor.
import numpy as np

N = 5
vetor = np.zeros(N)

print('Informe um valor para a posição:')
for i in range(0, N):
    vetor[i] = float(input(f'[{i}]: '))

maior = vetor[0]
menor = vetor[0]

for i in range(0, N):
    if maior < vetor[i]:
        maior = vetor[i]
    if menor > vetor[i]:
        menor = vetor[i]

print(f'O maior valor contido no vetor {vetor} é {maior} e o menor valor é {menor}.')

print('=)')