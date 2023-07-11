estrutura = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

print('Informe os valores da estrutura:')
for indice in range(18):
    estrutura[indice] = int(input('= '))

maior_valor = estrutura[0]
menor_valor = estrutura[0]
posicao_maior = 0
posicao_menor = 0

for indice in range(1, 18): 
    valor = estrutura[indice]
    if valor > maior_valor:
        maior_valor = valor
        posicao_maior = indice
    if valor < menor_valor:
        menor_valor = valor
        posicao_menor = indice

print(f'\nO maior valor armazenado na estrutura {estrutura} é [{maior_valor}] e está na posição [{posicao_maior}].')
print(f'O menor valor armazenado na estrutura {estrutura} é [{menor_valor}] e está na posição [{posicao_menor}].')

print('\n=)')