# Altere o algoritmo anterior para que ele realize o produto da primeira lista,
# pelo inverso da segunda lista.

lista_a = [0, 0, 0, 0, 0]
lista_b = [0, 0, 0, 0, 0]
lista_produto = [0, 0, 0, 0, 0]


print('Informe os valores para a primeria lista:')
for indice in range(0, len(lista_a)):
    lista_a[indice] = int(input(f'[{indice}]: '))

print('Informe os valores para a segunda lista:')
for indice in range(0, len(lista_b)):
    lista_b[indice] = int(input(f'[{indice}]: '))

for indice in range(0, len(lista_a)):
    lista_produto[indice] = lista_a[indice] * lista_b[len(lista_b - 1 - indice)]

print(f'\n{lista_a} * {lista_b} = {lista_produto}')

print('=)')