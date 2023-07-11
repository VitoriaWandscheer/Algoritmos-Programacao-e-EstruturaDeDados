# Faça um programa que permita ao usuário entrar com uma matriz de 3 x 3
# números inteiros.
# Em seguida, gere um array unidimensional pela soma dos
# números de cada coluna da matriz e mostrar na tela esse array. Por exemplo, a
# matriz:
#           5   -8  10
#           1    2  15
#          25   10  7
# Vai gerar um vetor, onde cada posição é a soma das colunas da matriz. A
# primeira posição será 5 + 1 + 25, e assim por diante:
#           31  4   3

def preenche_matriz():
    matriz = np.zeros((N,N)).astype(int)
    print('(Informe um valor para cada posição)')
    for linha in range(0, N):
        for coluna in range(0,N):
            matriz[linha][coluna] = int(input(f'[{linha}][{coluna}]: '))
    return matriz

def soma_colunas(matriz):
    array_unidimensional = []
    for coluna in range(0,N):
        soma = 0
        for linha in range(0,N):
            soma += matriz[linha][coluna]
        array_unidimensional.append(soma)
    return array_unidimensional

def mostra_resultado(matriz, array_unidimensional):
    print()
    print('~ A partir da matriz:')
    print(matriz)
    print()
    print(f'~ A soma das colunas da matriz é igual ao seguinte vetor:')
    print(array_unidimensional)

def assina():
    print()
    print('=)')
    print()

import numpy as np

N = 3
matriz = preenche_matriz()
print(matriz)
array_unidimensional = soma_colunas(matriz)
mostra_resultado(matriz, array_unidimensional)
assina()