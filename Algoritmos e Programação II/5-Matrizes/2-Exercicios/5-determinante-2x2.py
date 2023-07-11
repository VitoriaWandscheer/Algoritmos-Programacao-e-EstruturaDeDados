#Faça um algoritmo que lê uma matriz M2X2 que calcula e mostra o resultado do determinante desta matriz.
import numpy as np

N = 2                   ### TAMANHO DA MATRIZ
m = []                  ### MATRIZ
m = np.zeros((N, N))    ### PREENCHENDO MATRIZ COM 0s

dp = 0                  ### DIAGONAL PRINCIPAL
ds = 0                  ### DIAGONAL SECUNDARIA
determinante = 0

### RECEBENDO VALORES PARA MATRIZ LINHA POR LINHA ###
for l in range(len(m)):
    print(f'Informe os valores da linha {l}:')
    for c in range(len(m[l])):
        m[l][c] = int(input('= '))

### EFETUANDO OS CALCULOS ###
dp = m[0][0] * m[1][1]                  # CALCULANDO A DIAGONAL PRINCIPAL
ds = m[0][1] * m[1][0]                  # CALCULANDO A DIAGONAL SECUNDÁRIA
determinante = dp - ds                  # CALCULANDO O DETERMINANTE

print(f'A determinante da matriz informada é igual a {determinante}')

print('=)')