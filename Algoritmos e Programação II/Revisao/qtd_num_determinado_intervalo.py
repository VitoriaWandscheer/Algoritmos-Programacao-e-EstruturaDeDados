print('Quando encerrarem os valores digite um número negativo')
valor = 0
a = 0
b = 0
c = 0
d = 0

while valor >= 0:
    valor = int(input('Informe o valor: '))
    if (0 <= valor) and (valor < 25):
        a += 1
    elif (25 < valor) and (valor <= 50):
        b += 1
    elif (50 < valor) and (valor <= 75):
        c += 1
    elif (75 < valor) and (valor <= 100):
        d += 1
    elif (valor < 0):
        break

print(f'     Entre:         existem:')
print(f'    00 e 25           {a}')
print(f'    26 e 50           {b}')
print(f'    51 e 75           {c}')
print(f'    76 e 100          {d}')
print('=)')