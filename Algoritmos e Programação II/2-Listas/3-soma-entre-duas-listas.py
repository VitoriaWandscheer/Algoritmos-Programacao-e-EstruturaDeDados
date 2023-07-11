# Elabore um algoritmo que leia duas listas de 5 posições,
# após a leitura realizar a soma e imprima o resultado da soma entre as duas listas de inteiros.

lista_a = []
lista_b = list()
lista_soma = list()

for indice in range(0, 5):
    print('Informe os valores para a primeria e para a segunda lista:')
    aux_a = int(input(f'[{indice}]: '))
    lista_a.append(aux_a)
    aux_b = int(input(f'[{indice}]: '))
    lista_b.append(aux_b)

for indice in range(0, 5):
    aux_soma = lista_a[indice] + lista_b[indice]
    lista_soma.append(aux_soma)

print(f'\n{lista_a} + {lista_b} = {lista_soma}')

print('=)')