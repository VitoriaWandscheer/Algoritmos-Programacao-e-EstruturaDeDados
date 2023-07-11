capacidade = float(input('Informe a capacidade do elevador: '))

print('Informe as seguntes informações: ')

p1 = float(input('Peso da primeira pessoa: '))
p2 = float(input('Peso da segunda pessoa: '))
p3 = float(input('Peso da terceira pessoa: '))
p4 = float(input('Peso da quarta pessoa: '))
p5 = float(input('Peso da quinta pessoa: '))

if p1 + p2 + p3 + p4 + p5 <= capacidade:
    print('O elevador está liberado para subir.')
else:
    print('O elevador excedeu a capacidade máxima.')

print('=)')