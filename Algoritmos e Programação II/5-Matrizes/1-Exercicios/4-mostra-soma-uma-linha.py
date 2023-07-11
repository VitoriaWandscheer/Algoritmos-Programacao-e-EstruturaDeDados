# Faça um algoritmo que lê uma matriz M5x5.
# Calcular e mostrar a soma de todos os valores da linha 4.
import numpy as np

N = 5                   ### TAMANHO DA MATRIZ
L = 4                   ### LINHA A SER SOMADA
m = []                  ### MATRIZ
m = np.zeros((N, N))    ### PREENCHENDO MATRIZ COM 0s
vetor = np.zeros(N)     ### PREENCHENDO VETOR COM 0s

### RECEBENDO VALORES PARA MATRIZ LINHA POR LINHA ###
for l in range(len(m)):
    print(f'Informe os valores da linha {l}:')
    for c in range(len(m[l])):
        m[l][c] = int(input('= '))

### TRANSFORMANDO ALINHA A SER SOMADA EM VETOR ###
for i in range(N):
    vetor[i] = m[L][i]

### SOMANDO ELEMENTOS DO VETOR E EXIBINDO O RESULTADO ###
print(f'A soma dos valores {m[L]} é igual a {vetor.sum()}.')

print('=)')