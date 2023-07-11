m = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

print('Informe os valores da matriz:')
for linha in range(5):
    for coluna in range(5):
        m[linha][coluna] = int(input('= '))

menor = m[0][0]
maior = m[0][0]
posicao_maior = 0
posicao_menor = 0

for l in range(5):
    for c in range(5): 
        valor = m[l][c]
        if valor > maior:
            maior = valor
            posicao_maior = l

for i in range(5):
    valor = m[posicao_maior][i]
    if valor < menor:
        menor = valor
        posicao_menor = i

minimax = m[posicao_maior][posicao_menor]

print(f'De acordo com a matriz:')
for g in m:
    for elemento in g:
        print(int(elemento), end=' ')
    print()
print(f'\nSeu elemento minimax é {minimax}')

print('\n=)')