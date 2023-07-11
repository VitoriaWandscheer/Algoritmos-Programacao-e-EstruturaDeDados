# Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x
# e mostre os 10 valores armazenados.

x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for indice in range(0, len(x)):
    x[indice] = int(input(f'Informe o valor de [{indice}]: '))

print(f'Os valores armazenados em X são: {x}')

print('=)')