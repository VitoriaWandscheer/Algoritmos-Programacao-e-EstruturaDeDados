# Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x.
# Após completar toda a leitura da lista,
# verificar se cada valor armazenado na lista é par ou ímpar.
# Se for par, fazer com que o valor seja atualizado para
# o resultado da multiplicação do valor contido pelo índice.
# Se for impar fazer com que a lista receba o valor do seu próprio índice.

x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for indice in range(0, len(x)):
    x[indice] = int(input(f'Informe o valor de [{indice}]: '))

for indice in range(0, len(x)):
    if x[indice] % 2 == 0:
        x[indice] = indice * x[indice]
    if x[indice] % 2 != 0:
        x[indice] = indice

print(f'Os valores armazenados em X são: {x}')

print('=)')
