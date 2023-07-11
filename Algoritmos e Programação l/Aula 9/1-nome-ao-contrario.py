# Faça um programa que leia o nome do usuário
# e mostre o nome de trás para frente, utilizando somente letras maiúsculas. 

nome = list(input('Informe seu nome: \n'))                  # armazera em nome na variavel 'nome'
qtd = len(nome)
nome_cont = ''
x = 1

while x <= qtd:                                             # enquanto toda a variavel não for percorrida a sequencia se repetirá
    nome_cont = nome_cont + nome[-x]                        # concatena a string
    x += 1                                                  # contador conta mais uma repetição

print(nome_cont.upper())                                    # mostra o nome ao contrario em maiúscula

print('=)')                                                 # assinatura =)