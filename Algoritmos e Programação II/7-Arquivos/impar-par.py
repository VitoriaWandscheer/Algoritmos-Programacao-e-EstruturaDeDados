# Arquivos com números ímpares e pares

with open('impares.txt', 'w+') as impares, open('pares.txt', 'w+') as pares:
    impares.write('Lista de números IMPARES compreendidos entre 99 e 1001\n')
    pares.write('Lista de números PARES compreendidos entre 99 e 1001\n')
    for n in range(100,1001):
        if n % 2 == 0:
            pares.write(f"{n}\n")
        else:
            impares.write(f'{n}\n')

print('=)\n')