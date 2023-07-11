# Lê estrutura (lista, tupla ou conjunto), K que comporte 20 elementos.
# Troque a seguir os elementos de índice ímpar com os de índice par imediatamente seguinte
# mostre no final como ficou a estrutura K, com as alterações.

k = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print('Informe:')
for x in range(0, 20):
    k[x] = input('= ')

for y in range (0, 20, 2):
    aux = k[y]
    k[y] = k[y+1]
    k[y+1] = aux

print(k)