# Escreva um programa que leia duas strings.
# Verifique se a segunda ocorre na primeira e imprima
# a posição de início.
# Exemplo:
#	String 1: AABBEEEFAATT
#   String 2: BE
#   Resultado: BE encontrado na posição 3

primeira = str(input('Digite aqui o conteúdo a ser verificado:\n ')).lower()
segunda = str(input('Digite aqui o que será buscado no conteúdo informado:\n ')).lower()

if segunda in primeira:
    posição = primeira.find(segunda)
    print(f'"{segunda}" é encontrado na posição {posição}.')
else:
    print(f'"{segunda}" não ocorre em "{primeira}"')

print('=)')