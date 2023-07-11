estrutura = [0,0,0,0,0,0,0,0,0,0]

print('Informe os valores da estrutura:')
for indice in range(10):
    estrutura[indice] = int(input('= '))

aux = 0

for indice in range(10): 
    valor = estrutura[indice]   
    if valor <= 0:
        print(f'\n{estrutura[indice]} é menor ou igual a zero e está na posição [{indice}]')
        aux += 1
if aux == 0:
    print('Não há números menores ou iguais a zero.')

print('\n=)')