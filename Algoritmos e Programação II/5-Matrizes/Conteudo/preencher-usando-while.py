l = 0
# Inserindo dados na matriz usando while.
matriz = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
while l < len(matriz):
    c = 0
    while c < len(matriz[l]):
        matriz[l][c]= int(input("Informe valores para a matriz"))
        c +=1
    print()
    l += 1

print("Matriz 3x3: ", matriz)