# Faça um programa que leia um vetor(lista) de 5 posições
# e uma matriz de 5x 5 calcule
# e mostre o resultado da multiplicação do primeiro elemento do vetor, por toda a primeira linha da matriz,
# do segundo item do vetor por toda a segunda linha da matriz e assim sucessivamente.

import numpy as np

N = 5                   ### TAMANHO DA MATRIZ
m = []                  ### MATRIZ
m = np.zeros((N, N))    ### PREENCHENDO MATRIZ COM 0s

v = []
v = np.zeros(N)

resultado = []
resultado = np.zeros((N,N))

### RECEBENDO VALORES PARA MATRIZ LINHA A LINHA ###
print('Informe os valores para a matriz 5x5:')
for l in range(len(m)):
    print(f'Informe os valores da linha {l}:')
    for c in range(len(m[l])):
        m[l][c] = int(input('= '))

print('\nAgora informe os valores do vetor:')
for i in range(N):
    v[i] = int(input('= '))

### EFETUANDO OS CALCULOS ###
for l in range(N):
    for c in range(N):
        resultado[l][c] = v[l] * m[l][c]

### EXIBINDO NA TELA LINHA POR LINHA ###
for lista in resultado:
    for elemento in lista:
        print(int(elemento), end=' ')
    print()

print('=)')