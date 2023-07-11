# Faça um algoritmo que lê uma matriz M5X5
# e crie 2 vetores(listas) SL (soma das linhas) e SC (soma das colunas) com 5 posições cada.
# Adicionar aos vetores o resultado da soma das linhas e das colunas da matriz, no final mostrar os dois vetores.
import numpy as np

N = 5                   ### TAMANHO DA MATRIZ
m = []                  ### MATRIZ
m = np.zeros((N, N))    ### PREENCHENDO MATRIZ COM 0s

SL = []                 #### VETOR SL
SC = []                 #### VETOR SC
SL = np.zeros(N)        ### PREENCHENDO VETOR COM 0s
SC = np.zeros(N)        ### PREENCHENDO VETOR COM 0s

soma = 0

### RECEBENDO VALORES PARA MATRIZ LINHA A LINHA ###
for l in range(len(m)):
    print(f'Informe os valores da linha [{l}]:')
    for c in range(len(m[l])):
        m[l][c] = int(input('= '))

### EFETUANDO A SOMA DAS LINHAS ###
for l in range(N):
    for c in range(N):
        soma = soma + m[l][c]
    SL[l] = soma
    soma = 0

### EFETUANDO A SOMA DAS COLUNAS ###
for c in range(N):
    for l in range(N):
        soma = soma + m[l][c]
    SC[c] = soma
    soma = 0

### EXIBINDO NA TELA LINHA POR LINHA ###
print('De acordo com a matriz:\n')
for lista in m:
    for elemento in lista:
        print(int(elemento), end=' ')
    print()

print(f'\nA soma das linhas é igual ao vetor SL={SL}\ne a soma das colunas é igual ao vetor SC={SC}')

print('=)')

