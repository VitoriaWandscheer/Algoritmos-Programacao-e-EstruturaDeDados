# Escreva um algoritmo que leia três valores que formam uma data:
# dia, mês e ano. 
# O usuário deverá, então,
# informar o número de dias que deseja somar a esta data.
# Seu algoritmo deverá apresentar a data calculada.
# Considere que:
# - O usuário sempre informará uma data válida, não sendo necessário fazer este teste;
# - Considere que os anos são todos não-bissextos

print('Informe os seguintes dados: ')

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

soma = int(input('Quantos dias deseja adicionar a data informada?\n'))

total = dia + soma

match mes:
    case 1:
        if (total <= 31) :
            dia = total
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= 59):
            dia = total - 31
            mes = mes + 1
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= 90):
            dia = total - 59
            mes = mes + 2
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= 120):
            dia = total - 90
            mes = mes + 3
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= 150):
            dia = total - 120
            mes = mes + 4
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= 181):
            dia = total - 150
            mes = mes + 5
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= 211):
            dia = total - 181
            mes = mes + 6
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= 241):
            dia = total - 211 
            mes = mes + 7
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= 272):
            dia = total - 241
            mes = mes + 8
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= 303):
            dia = total - 272
            mes = mes + 9
        elif (total - 333):
            dia = total - 303
            mes = mes + 10
            print(f'{dia}/{mes}/{ano}')
        elif (total <= 364):
            dia = total - 333
            mes = mes + 11
            print(f'{dia}/{mes}/{ano}')
        else:
            ano = ano + 1
    case 2:
        if (total <= 28) :
            dia = total
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= (28+31)):
            dia = total - 28
            mes = mes + 1
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= (28+31+30)):
            dia = total - (28+31)
            mes = mes + 2
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= (28+31+30+31)):
            dia = total - (28+31+30)
            mes = mes + 3
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= (28+31+30+31+30)):
            dia = total - (28+31+30+31)
            mes = mes + 4
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= (28+31+30+31+30+31)):
            dia = total - (28+31+30+31+30)
            mes = mes + 5
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= (28+31+30+31+30+31+31)):
            dia = total - (28+31+30+31+30+31)
            mes = mes + 6
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= (28+31+30+31+30+31+31+30)):
            dia = total - (28+31+30+31+30+31+31) 
            mes = mes + 7
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= (28+31+30+31+30+31+31+30+31)):
            dia = total - (28+31+30+31+30+31+31+30)
            mes = mes + 8
            print(f'{dia}/0{mes}/{ano}')
        elif (total <= (28+31+30+31+30+31+31+30+31+30)):
            dia = total - (28+31+30+31+30+31+31+30+31)
            mes = mes + 9
        elif (total - (28+31+30+31+30+31+31+30+31+30+31)):
            dia = total - (28+31+30+31+30+31+31+30+31+30)
            mes = mes + 10
            print(f'{dia}/{mes}/{ano}')
        else:
            ano = ano + 1

print('=)')