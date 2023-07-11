#Faça um programa que preencha dois vetores de dez elementos numéricos cada um
# e mostre o vetor resultante da intercalação deles:
import numpy as np
N = 10
NAB = 20
vetor_a  = []
vetor_b = []
vetor_ab = []
vetor_a = np.zeros(N, dtype=int)
vetor_b = np.zeros(N, dtype=int)
vetor_ab = np.zeros(NAB, dtype=int)

print('======== Informe os valores para o vetor A ========')
cont = 0
for indice_a in range(0,N):
    vetor_a[indice_a] = int(input('= '))
    vetor_ab[cont] = vetor_a[indice_a]
    cont += 2

print('======== Informe os valores para o vetor B ========')
cont = 1
for indice_b in range(0,N):
    vetor_b[indice_b] = int(input('= '))
    vetor_ab[cont] = vetor_b[indice_b]
    cont += 2

print('======== O vetor resultante da itercalação ========\n========           entre A e B é           ========\n',vetor_ab)

print('=)')