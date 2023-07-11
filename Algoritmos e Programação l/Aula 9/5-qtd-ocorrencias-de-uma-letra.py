# Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#  a) quantos espaços em branco existem na frase.
#  b) quantas vezes aparecem as vogais a, e, i, o, u.

frase = list(input('Informe uma frase:\n'))
lista = ['a', 'e', 'i', 'o', 'u', ' ']

for x in lista:
    print(f'A contagem de {x} = {frase.count(x)}')

print('=)')