# Faça um algoritmo que lê 10 valores para uma variável do tipo vetor de nome x
# e mostra os 10 valores armazenados na estrutura.
import numpy as np
# Tamanho da Array
N = 10

# Preenche a estrutura com zeros do tipo inteiro
vetor = np.zeros(N, dtype=int)

# Percorre a array, recebendo no indice [i] o valor informado pelo usuário
for i in range(0, N):
    vetor[i] = float(input(f'Informe um valor para a posição [{i}]: '))

# Percorre a array, mostrando o valor armazenado no indice [i] 
for i in range(0, N):
    print(f'O valor armazenado na posição [{i}] é {vetor[i]}')

print('=)')