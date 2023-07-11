import numpy as np

N = 3
nota = np.zeros(N)
print(type(nota))

print('Informe a nota do aluno: ')

for i in range(0, N, 1):
    nota[i] = float(input(f'Aluno {i}: '))

for i in range(0, N):
    print(f'O aluno {i} possui a nota {nota[i]}.')

print('=)')