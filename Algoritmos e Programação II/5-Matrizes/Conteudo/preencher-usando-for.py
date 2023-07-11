matriz = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]

# Inserindo dados na matriz usando for.
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
            matriz[l][c] = int(input("Informe valor para a matriz"))

print("Matriz 3x3: ", matriz)