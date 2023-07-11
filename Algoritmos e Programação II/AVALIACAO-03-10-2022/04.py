lista = [0,0,0]
m = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

print('Informe os valores da matriz:')
for linha in range(3):
    for coluna in range(4):
        m[linha][coluna] = int(input('= '))

print('\nAgora informe os valores da lista:')
for indice in range(3):
    lista[indice] = int(input('= '))

for x in range(3):
    aux = m[x][1]
    m[x][1] = lista[x]
    lista[x] = aux

print('\nA matriz após a troca é a seguinte:')
for l in m:
    for elemento in l:
        print(int(elemento), end=' ')
    print()

print(f'A lista após a troca é a seguinte:\n{lista}')

print('\n=)')