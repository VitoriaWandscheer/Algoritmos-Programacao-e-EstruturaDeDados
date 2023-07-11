matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz 3x3: ", matriz)
# Exibindo a matriz com for.
print("Matriz impressa de outra forma:")
for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
    print()

l = 0
# Exibindo a matriz com while.
print("Matriz impressa de outra forma:")
while l < len(matriz):
    c = 0
    while c < len(matriz[l]):
        print(matriz[l][c], end=' ')
        c +=1
    print()
    l += 1