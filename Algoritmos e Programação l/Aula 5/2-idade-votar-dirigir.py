# Faça um programa que receba o ano de nascimento de uma pessoa, calcule e mostre:
# Se ele já tem idade para votar (16 anos ou mais);
# E para conseguir carteira de habilitação (18 anos ou mais);

ano_nasc =  int(input('Informe o ano de nascimento: '))
ANO_ATUAL = 2022
VOTAR = 16
DIRIGIR = 18

idade = ANO_ATUAL - ano_nasc

if idade >= VOTAR :
    print('Já tem idade para votar.')
else :
    print('Não tem idade para votar.')

if idade >= DIRIGIR:
    print('Já tem idade para conseguir carteira de habilitação.')
else :
    print('Não tem idade para conseguir carteira de habilitação.')

print('=)')