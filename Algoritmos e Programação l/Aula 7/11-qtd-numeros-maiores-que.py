# Escreva um algoritmo que receba 15 números
# e imprima quantos números maiores que 30 foram digitados. 

cont = 0

for x in range(0,15, 1):
    var = int(input('Digite um numero:\n'))
    if var > 30:
        cont += 1
    
print(cont)

print('=)')