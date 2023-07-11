# Construa um algoritmo para calcular a distância entre dois pontos do plano cartesiano.
# Cada ponto é um par ordenado (x,y).
# dAB² = (xB – xA)² + (yB – yA)²

x1 = float(input('Informe o valor de x do primeiro par ordenado: '))
y1 = float(input('Informe o valor de y do primeiro par ordenado: '))
x2 = float(input('Informe o valor de x do segundo par ordenado: '))
y2 = float(input('Informe o valor de y do segundo par ordenado: '))

dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 # Elevar a 0.5 é o mesmo que a raiz quadrada.

print (f'A distância entre o ponto x e o ponto y é igual a {dist}.')

print('=)')