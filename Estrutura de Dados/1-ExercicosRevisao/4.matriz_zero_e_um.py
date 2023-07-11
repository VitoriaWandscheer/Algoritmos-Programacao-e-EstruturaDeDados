# Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os
# demais elementos. Escreva ao final a matriz obtida.
import numpy as np

def preenche_diagonal_principal(matriz):
    for posicao in range(0,N):
        matriz[posicao][posicao] = 1
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

N = 5
matriz = np.zeros((N,N))
mostra_matriz(preenche_diagonal_principal(matriz))
assina()