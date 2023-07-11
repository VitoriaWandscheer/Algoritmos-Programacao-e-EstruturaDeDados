# Elabore um algoritmo que leia 
# o nome e o ano de nascimento de uma pessoa
# e mostre qual é a sua idade atual. 

nome = str(input('Olá, digite o nome: '))
ano_nasc = int(input('Agora digite o ano de nascimento: '))

ANO_ATUAL = 2022

idade = ANO_ATUAL - ano_nasc

print (f'{nome} tem {idade} anos.')

print('=)')