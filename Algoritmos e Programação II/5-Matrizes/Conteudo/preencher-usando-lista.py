matriz = []

# Inserindo dados na matriz usando for através da linha.
for l in range(3):
    lista = []
    for c in range(3):
        lista.append(int(input("Informe valores para a matriz")))
    matriz.append(lista)

print("Matriz 3x3: ", matriz)