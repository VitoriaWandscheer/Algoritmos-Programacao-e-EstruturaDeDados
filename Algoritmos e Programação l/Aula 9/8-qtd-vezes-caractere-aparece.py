# Escreva um programa que leia uma string
# e imprima quantas vezes cada caractere aparece nessa string.
# Exemplo:
#	String 1: TTAC
# Resultado: 
# T:  2x
# A: 1x
# C: 1x

frase = input('Informe o conteúdo que deseja verificar:\n ').upper()

for x in frase:
    if(frase.count(x) != 0):
        print(f'{x} aparece {frase.count(x)} veze(s).')
        frase = frase.replace(x, '')

print('=)')