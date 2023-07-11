# Faça um programa que preencha duas estruturas (lista, tupla ou conjunto), X e Y,
# com dez números inteiros cada. Calcule e mostre os seguintes o seguinte resultado:
# A diferença entre X e Y
x = set()
y = set()

print('Informe os valores de X: ')
for i in range(0, 10):
    x.add(int(input('= ')))

print('Agora informe os valores de Y: ')
for indice in range(0, 10):
    y.add(int(input('= ')))

print(f'A diferença entre x={x} e y={y} é x-y={x-y}')