# Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da
# forma:

# A[i][j] = 2*i + 7*j se i < j
# A[i][j] = 3*i^2 se i = j
# A[i][j] = 4*i^3 + 5*j^2 + 1 se i > j

import numpy as np

def preenche_com_regras(matriz):
    for i in range(0,N):
        for j in range(0,N):
            if i < j:
                matriz[i][j] = ((2*i) + (7*j))
            elif i == j:
                matriz[i][j] = (3*(i**2))
            elif i > j:
                matriz[i][j] = (4*(i**3)) + (5*(j**2))
    return matriz

def mostra_matriz(matriz):
    print()
    print('~ MATRIZ RESULTANTE:')
    print()
    print(matriz)

def assina():
    print()
    print('=)')
    print()

N = 10
matriz = np.zeros((N,N))
mostra_matriz(preenche_com_regras(matriz))
assina()