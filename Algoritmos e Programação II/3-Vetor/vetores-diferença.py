# Faça um programa que preencha dois vetores, X e Y, com dez números inteiros cada.
# Calcule e mostre os seguintes vetores resultantes:
# A diferença entre X e Y
import numpy as np

x = []
y = []
d = []
N = 10
x = np.zeros(N, dtype=int)
y = np.zeros(N, dtype=int)
d = list()

print('============== Informe os valores de X ====================')
for indice in range(0, N):
    x[indice] = input('= ')
print('============== Informe os valores de Y ====================')
for indice in range(0, N):
    y[indice] = input('= ')

for ix in range(0, N):
    diferente = 0
    for iy in range(0, N):
        if x[ix] != y[iy]:
            diferente += 1
        if diferente == 10:
            d.append(x[ix])

for iy in range(0, N):
    diferente = 0
    for ix in range(0, N):
        if y[iy] != x[ix]:
            diferente += 1
        if diferente == 10:
            d.append(y[iy])
print('==========================================================')
print(f'A difereça entre os vetores X e Y é o vetor:\n{d}')

print('=)')