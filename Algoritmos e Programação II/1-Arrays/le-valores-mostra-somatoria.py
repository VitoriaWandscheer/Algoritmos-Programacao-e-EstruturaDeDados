# Faça um algoritmo que lê 5 valores para uma variável do tipo vetor
# e determine o somatório de todos valores armazenados no vetor.

import numpy as np

N = 5                              # Tamanho da Array
vetor = np.zeros(N, dtype=int)     # Preenche a estrutura com zeros do tipo inteiro
soma = 0

print('Informe um valor para a posição ')

for i in range(0, N):                       # Percorre a array
    vetor[i] = float(input(f'[{i}]: '))     # Recebe, no indice i, o valor informado pelo usuário
    soma = soma + vetor[i]                  # Soma o vetor[i] com a variavel soma, e armazena esse valor na variavel soma

print(f'A soma dos valores armazenados no vetor {vetor} é igual a {soma}.')

print('=)')