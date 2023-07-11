# Faça um algoritmo que lê uma matriz M5x5 e mostrar os valores da diagonal principal.

import numpy as np

N = 5                   ### TAMANHO DA MATRIZ
m = []                  ### MATRIZ
m = np.zeros((N, N))    ### PREENCHENDO VETOR COM 0s

### RECEBENDO VALORES PARA MATRIZ LINHA POR LINHA ###
for l in range(len(m)):
    for c in range(len(m[l])):
        m[l][c] = int(input('= '))

### MOSTRANDO OS VALORES DA DIAGONAL PRINCIPAL ###
for i in range(N):
    print(m[i][i])
    
print('=)')