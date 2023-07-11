# Ler uma estrutura (lista, tupla ou conjunto), R de 5 elementos, inteiros, contendo o resultado da LOTO.
# A seguir ler outra estrutura (lista, tupla ou conjunto), A de 10 elementos inteiros contendo uma aposta.
# A seguir imprima quantos pontos fez o apostador.

R = set()               # lista contendo os números da LOTO
A = set()               # Conjunto contendo os números de uma aposta
pontuação = set()          # lista para armazenar os numeros que o apostador acertou

print('Informe o resultado da LOTO $-$')
for x in range(0, 5):
    R.add(int(input('= ')))

print('\nInforme os valores da aposta:')
for y in range(0, 10):
    A.add(int(input('= ')))

pontuação = R & A

if len(pontuação) != 0:
    if len(pontuação) != 1:
        print(f'Parabéns! Acertou os números {pontuação}, acumulando assim {len(pontuação)} pontos.')
    else: 
        print(f'Parabéns! Acertou o número {pontuação}, acumulando assim {len(pontuação)} ponto.')
else:
    print(f'Sinto muito, não acertou nenhum número, portanto não acumulou pontos.')

print('=)')