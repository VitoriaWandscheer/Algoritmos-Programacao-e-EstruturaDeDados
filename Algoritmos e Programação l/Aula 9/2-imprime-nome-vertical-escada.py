#Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada,
# usando apenas letras maiúsculas. 
#Exemplo: Nome = RAFAEL
#Resultado gerado pelo programa: 
#R
#RA
#RAF
#RAFA
#RAFAE
#RAFAEL

nome = list(input('Informe o nome: '))
qtd = len(nome)
x = 0
imprimir = ''

while x <= qtd:
    imprimir = imprimir + nome[x]
    print(imprimir.upper())
    x += 1

print('=)')