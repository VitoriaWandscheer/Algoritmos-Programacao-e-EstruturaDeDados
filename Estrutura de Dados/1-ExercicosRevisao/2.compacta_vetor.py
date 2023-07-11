# Faça um programa que leia um vetor de 15 posições e o compacte, ou seja,
# elimine as posições com valor zero armazenado. Para isso, todos os elementos
# à frente do valor zero, devem ser movidos uma posição para trás no vetor. Ao
# final exiba o vetor resultante.

def preenche_lista():
    vetor = []
    print('(Informe um valor para cada posição)')
    for i in range(0, N):
        vetor.append(float(input(f'[{i}]: ')))
    return vetor

def compacta_lista(vetor):
    while 0 in vetor:
        vetor.remove(0)
    return vetor

def mostra_lista(vetor):
    print()
    print('~ VETOR COMPACTO:')
    print()
    print(vetor)

def assina():
    print()
    print('=)')
    print()

N = 15
vetor = preenche_lista()
compacta_lista(vetor)
mostra_lista(vetor)
assina()