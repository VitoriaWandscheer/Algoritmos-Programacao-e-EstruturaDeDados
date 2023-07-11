# Faça um algoritmo que lê uma matriz M5x5.
# A matriz deve ser preenchida através das colunas, por exemplo, se for digitado:
# 1,2,3,4,5,6,7,8,9,10,... 
# Após mostre a matriz resultante.
import numpy as np

N = 5                   ### TAMANHO DA MATRIZ
m = []                  ### MATRIZ
m = np.zeros((N, N))    ### PREENCHENDO MATRIZ COM 0s
coluna = 0              ### COLUNA A SER PREENCHIDA

### RECEBENDO VALORES PARA MATRIZ COLUNA POR COLUNA ###
while coluna < N:
    for l in range(len(m)):
        m[l][coluna] = int(input('= '))
    coluna += 1

### EXIBINDO NA TELA LINHA POR LINHA ###
for lista in m:
    for elemento in lista:
        print(int(elemento), end=' ')
    print()

print('=)')