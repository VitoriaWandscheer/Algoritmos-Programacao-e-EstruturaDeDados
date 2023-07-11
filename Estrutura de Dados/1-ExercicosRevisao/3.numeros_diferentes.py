# Faça um programa para ler 10 números DIFERENTES a serem armazenados
# em um vetor. Os dados deverão ser armazenados no vetor na ordem que
# forem sendo lidos, sendo que caso o usuário digite um número que já foi
# digitado anteriormente, o programa
# deverá pedir para ele digitar outro número. Note que cada valor digitado pelo
# usuário deve ser pesquisado no vetor, verificando se ele existe entre os
# números que já foram fornecidos. Exibir na tela o vetor final que foi digitado.

import numpy as np

def preenche_lista():
    lista = np.zeros(N)
    print('(Informe um valor para cada posição)')
    for i in range(0, N):
        lista = verifica_numero(i, lista)
    return lista

def verifica_numero(posicao, lista):
    numero = int(input(f'[{posicao}]: '))
    while numero in lista:
        print('}  DIGITE UM NÚMERO DIFERENTE   {')
        print('} Esse numero já foi informado. {')
        numero = int(input(f'[{posicao}]: '))
    lista[posicao] = numero
    return lista

def mostra_lista(lista):
    print()
    print('~ VETOR INFORMADO:')
    print()
    print(lista)
    print()
    print('Apenas com números diferentes =)')

def assina():
    print()
    print('=)')
    print()

N = 10
print('Informe dez (10) números diferentes =)')
lista = preenche_lista()
mostra_lista(lista)
assina()