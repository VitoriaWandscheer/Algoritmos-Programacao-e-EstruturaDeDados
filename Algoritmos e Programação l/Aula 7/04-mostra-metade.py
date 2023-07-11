# Escreva um algoritmo que leia dez números do usuário
# e imprima a metade de cada número. 

x = 0
print('Informe dez números: ')
while x < 10: 
    num_usuario = int(input('= '))
    metade = num_usuario / 2
    print(metade)
    x += 1

print('=)')