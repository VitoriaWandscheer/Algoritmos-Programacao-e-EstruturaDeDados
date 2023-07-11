#Faça um algoritmo que lê uma matriz M5x5 e mostrar os valores digitados para a matriz M.
import numpy as np

N = 5                   ### DTAMANHO DA MATRIZ
m = []                  ### MATRIZ
m = np.zeros((N, N))    ### PREENCHENDO MATRIZ COM 0s

### RECEBENDO VALORES PARA MATRIZ LINHA A LINHA ###
for l in range(len(m)):
    for c in range(len(m[l])):
        m[l][c] = int(input('= '))

### EXIBINDO NA TELA LINHA POR LINHA ###
for lista in m:
    for elemento in lista:
        print(int(elemento), end=' ')
    print()

print('=)')