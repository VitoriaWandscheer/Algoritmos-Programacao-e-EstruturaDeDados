# Faça um algoritmo que lê uma matriz M10x10. 
# Troque a seguir os valores contidos na linha de índice 2 com os da linha de índice 8
# e também troque os valores da linha de índice 5 com os da coluna de índice 9.
# No final mostre a matriz.

import numpy as np

N = 10                  ### TAMANHO DA MATRIZ
m = []                  ### MATRIZ
m = np.zeros((N, N))    ### PREENCHENDO MATRIZ COM 0s
aux = 0

### RECEBENDO VALORES PARA MATRIZ LINHA A LINHA ###
for l in range(len(m)):
    print(f'Informe os valores da linha [{l}]:')
    for c in range(len(m[l])):
        m[l][c] = int(input('= '))


### ARMAZENA EM UMA VARIAVEL AUXILIAR E DEPOIS SUBSTITUI DE ACORDO COM O QUE É SOLICITADO NA QUESTÃO ###
for c in range(len(m)):
    aux = m[2][c]
    m[2][c] = m[8][c]
    m[8][c] = aux
for z in range(len(m)):
    aux = m[5][z]
    m[5][z] = m[z][9]
    m[z][9] = aux

### EXIBINDO NA TELA LINHA POR LINHA ###
for lista in m:
    for elemento in lista:
        print(int(elemento), end=' ')
    print()

print('=)')