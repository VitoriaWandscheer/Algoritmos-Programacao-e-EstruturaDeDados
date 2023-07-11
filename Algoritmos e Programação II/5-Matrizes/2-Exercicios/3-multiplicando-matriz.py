# Faça um algoritmo que lê valores para uma matriz M4X4
# e um valor para a variável “a” (do tipo simples, pode ser: inteiro, float).
# Multiplicar cada valor contido na matriz pelo valor da variável e colocar os resultados num vetor(lista) V com 16 elementos.
# Mostre no final o vetor(lista).
import numpy as np

N = 4                   ### TAMANHO DA MATRIZ
m = []                  ### MATRIZ
m = np.zeros((N, N))    ### PREENCHENDO MATRIZ COM 0s
a = int(input('Informe o valor de a:\n= '))
V = 16
vetor = []
vetor = np.zeros(V)
i = 0

### RECEBENDO VALORES PARA MATRIZ LINHA A LINHA ###
for l in range(len(m)):
    print(f'Informe os valores da linha [{l}]:')
    for c in range(len(m[l])):
        m[l][c] = int(input('= '))

### EFETUANDO A MULTIPLICAÇÃO E ARMZENANDO EM vetor ### 
for l in range(N):
    for c in range(N):
        vetor[i] = a * m[l][c]
        i += 1

print(f'\nO vetor resultante é o seguinte:\n{vetor}')

print('=)')