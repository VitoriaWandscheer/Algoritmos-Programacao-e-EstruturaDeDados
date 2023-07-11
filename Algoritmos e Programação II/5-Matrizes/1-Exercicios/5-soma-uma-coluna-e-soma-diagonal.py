# Faça um algoritmo que lê valores para uma matriz M10x10 calcular e mostrar:
# O somatório dos valores da coluna 2
# O somatório dos valores da diagonal principal
import numpy as np

N = 3                   ### TAMANHO DA MATRIZ
C = 2                   ### COLUNA A SER SOMADA
m = []                  ### MATRIZ
m = np.zeros((N, N))    ### PREENCHENDO MATRIZ COM 0s
vetor = np.zeros(N)     ### PREENCHENDO VETOR COM 0s

### RECEBENDO VALORES PARA MATRIZ LINHA POR LINHA ###
for l in range(len(m)):
    print(f'Informe os valores da linha {l}:')
    for c in range(len(m[l])):
        m[l][c] = int(input('= '))

### TRANSFORMANDO A COLUNA A SER SOMADA EM VETOR E FAZENDO A SOMA ###
for i in range(N):
    vetor[i] = m[i][C]
soma_coluna = vetor.sum()

### TRANSFORMANDO A DIAGONAL PRINCIPAL EM VETOR E FAZENDO A SOMA ###
for i in range(N):
    vetor[i] = m[i][i]

### EXIBINDO O RESULTADO NA TELA ###
print(f'A soma dos valores armazenados na coluna {C} é igual a {soma_coluna}\ne a soma da diagonal principal é {vetor.sum()}.')

print('=)')