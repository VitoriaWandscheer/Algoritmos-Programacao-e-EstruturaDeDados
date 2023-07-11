# Escreva um algoritmo que receba cinco números do usuário
# e imprima o cubo de cada número. 

x = 0
print('Informe cinco números: ')
while x < 5: 
    num_usuario = int(input('= '))
    cubo = num_usuario ** 3
    print(cubo)
    x += 1

print('=)')