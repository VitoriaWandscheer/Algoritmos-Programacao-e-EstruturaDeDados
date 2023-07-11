# Ler 2 vetores, R de 5 elementos e S de 10 elementos, ambos de inteiros.
# Gere um vetor X que possua os elementos comuns a R e a S.
# Considere que no mesmo vetor não haverá números repetidos.
import numpy as np

NR = 5
r = []
r = np.zeros(NR, dtype=int)
NS = 10
s = []
s = np.zeros(NS, dtype=int)
x = []
x = np.zeros(NR, dtype=int)
cont = 0

print('Informe os 5 valores para o vetor R:')
for indice_r in range(0,NR):
    r[indice_r] = int(input('= '))
print('\nInforme os 10 valores para o vetor S:')
for indice_s in range(0,NS):
    s[indice_s] = int(input('= '))

for indice_r in range(0, NR):
    for indice_s in range(0, NS):
        if r[indice_r] == s[indice_s]:
            x[cont] = s[indice_s]
            cont += 1

print(f'O vetor contendo os elementos comuns a R e S é X ={x}') 

print("=)")