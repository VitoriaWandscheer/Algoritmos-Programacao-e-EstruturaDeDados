#Ler um vetor R de 5 elementos, inteiros, contendo o resultado da LOTO.
# A seguir ler um vetor A de 10 elementos inteiros contendo uma aposta.
# A seguir imprima quantos pontos fez o apostador.
import numpy as np

NR = 5
r = []
r = np.zeros(NR, dtype=int)

NA = 10
a = []
a = np.zeros(NA, dtype=int)

pontos = list()

print('Informe o resultado da LOTO $-$')
for indice_r in range(0,NR):
    r[indice_r] = int(input('= '))

print('\nInforme os valores da aposta:')
for indice_a in range(0,NA):
    a[indice_a] = int(input('= '))

for indice_r in range(0, NR):
    for indice_a in range(0, NA):
        if r[indice_r] == a[indice_a]:
            pontos.append(r[indice_r])

if len(pontos) != 0:
    if len(pontos) != 1:
        print(f'Parabéns! Acertou os números {pontos}, acumulando assim {len(pontos)} pontos.')
    else: 
        print(f'Parabéns! Acertou o número {pontos}, acumulando assim {len(pontos)} ponto.')
else:
    print(f'Sinto muito, não acertou nenhum número, portanto não acumulou pontos.')

print('=)')