# Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa.
# Por exemplo: OSSO e OVO são palíndromos.
# Em textos mais complexos os espaços e pontuação são ignorados.
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
# Faça um programa que leia uma sequência de caracteres,
# mostre-a e diga se é um palíndromo ou não.

sequencia = str(input('Informe o conteudo que deseja saber se é um palindromo ou não:\n')).lower()
original = sequencia

sequencia = sequencia.replace(" ", "")      #Substitui os espaços em branco pelo vazio.
qtd = len(sequencia)                        #conta o numero de caracteres.
seq_contrario = ''                          #variavel que irá armazenar a sequencia ao contrario.
x = 1                                       #contador e acumulador

while x <= qtd:                                         #enquanto não for percorrida toda a extenção da string a condição se repetirá.
    seq_contrario = seq_contrario + sequencia[-x]       #Adiciona a variavel 'seq_contrario' uma letra por vez, de tras para frente, invertendo assim a string
    x += 1                                              #contador

'''frase[::-1]'''

if sequencia == seq_contrario:
    print(f'"{original}" é um palíndromo.')
else:
    print(f'"{original}" não é um palíndromo.')

print('=)')