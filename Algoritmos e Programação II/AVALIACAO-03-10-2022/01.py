A = [0, 0, 0]
B = [0, 0, 0]

print('\nInforme os valores para A:')
for indice in range(3):
    A[indice] = int(input('= '))

print('\nInforme os valores para B:')
for indice in range(3):
    B[indice] = int(input('= '))

print('\nOs valores informados, na ordem inversa, são os seguintes:')
print('Estrutura A:')
for x in range(3):
    print(A[2 - x])

print('Estrutura B:')
for y in range(3):
    print(B[2 - y])

print('\n=)')