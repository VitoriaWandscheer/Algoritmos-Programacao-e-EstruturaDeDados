import numpy as np
N = 6
vetor = np.zeros(N)
print(type(vetor))

for i in range (N):
    vetor[i] = float(input(f'Informe um valor para V[{i}]: '))

print(vetor)

print('=)')