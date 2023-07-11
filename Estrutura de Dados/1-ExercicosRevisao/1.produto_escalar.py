# Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o
# produto escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os
# dois conjuntos e o produto escalar, sendo que o produto escalar é dado por:
# x1 ∗ y1 + x2 ∗ y2 + ... + xn ∗ yn

import numpy as np

def preenche_vetor():
    vetor = np.zeros(N)
    print('(Informe um valor para cada posição)')
    for i in range(0, N):
        vetor[i] = float(input(f'[{i}]: '))
    return vetor

def calcula_escalar(a,b):
    resultado = 0
    for i in range(0, N):
        resultado += a[i] * b[i]
    return resultado

def mostra_resultado(vetor_a,vetor_b,produto_escalar):
    print()
    print('~ A partir dos conjuntos:')
    print(vetor_a,' e ', vetor_b)
    print()
    print(f'O produto escalar é igual a [{produto_escalar}]')

def assina():
    print()
    print('=)')
    print()

N = 5

print('~ A partir dos vetores informados retornaremos o Produto Escalar ~')
print()
print('~ Primeiro Vetor: ')
vetor_a = preenche_vetor()
print()
print('~ Segundo Vetor: ')
vetor_b = preenche_vetor()
produto_escalar = calcula_escalar(vetor_a, vetor_b)

mostra_resultado(vetor_a, vetor_b, produto_escalar)
assina()