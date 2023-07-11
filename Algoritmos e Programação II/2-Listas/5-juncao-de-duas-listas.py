# Faça um algoritmo que lê duas listas A e B com 5 elementos cada.
# Construir uma lista C, sendo este a junção das duas outras listas,
# ou seja, a lista C deverá conter 10 elementos. Mostre no final a lista C.

lista_a = list()
lista_b = list()
lista_c = list()

print('Informe os valores para a primeria lista:')
for indice in range(0, 5):
    aux_a = int(input(f'[{indice}]: '))
    lista_a.append(aux_a)
    print(lista_a)

print('Informe os valores para a segunda lista:')
for indice in range(0, 5):
    aux_b = int(input(f'[{indice}]: '))
    lista_b.append(aux_b)

for y in range(0, 5):
    lista_c.append(lista_a[y])

for y in range(0, 5):
    lista_c.append(lista_b[y])

print(lista_c)

print('=)')