# Faça um programa que preencha um vetor com 9 números inteiros,
# calcule e mostre os que são números primos e suas respectivas posições.
import numpy as np
# Criando um Vetor
N = 9
vetor = []
vetor = np.zeros(N, dtype=int)
#Lista para armazenar os numeros primos e suas respectivas posições
lista_primos = list()
#recebe os valores e verifica se são primos, caso sejam, armazena em lista_primos os numeros primos e suas respectivas posições
for indice in range(0,9):
    vetor[indice] = int(input('= '))
    numero = int(vetor[indice])
    cont = 0
    for x in range(2, numero):
        if numero % x == 0:
            cont += 1
    if cont == 0 and numero != 1:
        lista_primos.append(numero)
        lista_primos.append(indice)
#Se houverem numeros primos, mostra quais são e as posições, caso não apresenta uma mensagem em negativa
if len(lista_primos) != 0:
    print(f'Dentre os valores {vetor}, são números primos e suas respectivas posições:')
    qtd = int(len(lista_primos))
    for x in range(0, qtd, 2):
        print(f'Número: {lista_primos[x]}           Posição: {lista_primos[x+1]}')
else:
    print(f'Dentre os valores [{vetor}], não há números primos.')

print('=)')