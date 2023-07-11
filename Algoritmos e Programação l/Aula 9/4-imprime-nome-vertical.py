#aça um programa que solicite o nome do usuário e imprima-o na vertical.
#Exemplo: Nome = Lidiane
#Resultado gerado pelo programa: 
#L
#I
#D
#I
#A
#N
#E

nome = list(input('Informe seu nome:\n'))
qtd = len(nome)
x = 0

while x < qtd:
    print(nome[x].upper())
    x += 1

print('=)')