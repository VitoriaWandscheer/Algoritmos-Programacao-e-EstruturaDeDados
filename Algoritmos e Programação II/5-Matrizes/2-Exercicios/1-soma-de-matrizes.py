# Faça um algoritmo que receba um valor N correspondente ao tamanho de duas matrizes quadradas de ordem N (MNxN). 
# Leia os valores inteiros para preencher todas as posições de cada uma das matrizes, e calcule a SOMA das matrizes.

import numpy as np

N = int(input('Informe o valor de N(tamanho da matriz quadrada):\n='))                   ### TAMANHO DA MATRIZ
ma = []                 ### MATRIZ A
mb = []                 ### MATRIZ B
ms = []                 ### MATRIZ SOMA
ma = np.zeros((N, N))   ### PREENCHENDO MATRIZ COM 0s
mb = np.zeros((N, N))   ### PREENCHENDO MATRIZ COM 0s
ms = np.zeros((N, N))   ### PREENCHENDO MATRIZ COM 0s


### RECEBENDO VALORES PARA MATRIZ LINHA A LINHA ###
print("MATRIZ A")
for l in range(len(ma)):
    print(f'Informe os valores da linha [{l}]:')
    for c in range(len(ma[l])):
        ma[l][c] = int(input('= '))

print("MATRIZ B")
for l in range(len(mb)):
    print(f'Informe os valores da linha [{l}]:')
    for c in range(len(mb[l])):
        mb[l][c] = int(input('= '))

### REALIZANDO A SOMA DAS MATRIZES ma e mb e armazenando em MS ###

for l in range(N):
    for c in range(N):
        ms[l][c] = ma[l][c] + mb[l][c]


### EXIBINDO NA TELA LINHA POR LINHA ###
print('A soma das matrizes informadas é igual a seguinte matriz:')
for lista in ms:
    for elemento in lista:
        print(int(elemento), end=' ')
    print()

print('=)')