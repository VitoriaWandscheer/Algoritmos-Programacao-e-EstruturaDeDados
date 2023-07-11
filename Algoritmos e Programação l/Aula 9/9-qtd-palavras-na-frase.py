# Escreva um programa que recebe uma frase
# e retorna o número de palavras que a frase contém.
# Considere que a palavra pode começar e/ou terminar por espaços. 

frase = input('Informe uma frase:\n ').strip(' ')
lista = frase.split()
print(f'Há {len(lista)} palavras na frase "{frase}"')

print('=)')