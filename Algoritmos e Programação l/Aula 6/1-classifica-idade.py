#Elabore um algoritmo que leia a idade e o sexo de uma pessoa.
#Mostre a mensagem conforme a tabela abaixo:

idade = int(input('Informe sua idade: '))
sexo = str(input('Informe\nM para maculino e F para feminino:\n '))

if sexo == 'F' or sexo == 'f':
    if idade <=12 :
        print('Menina')
    elif idade <= 24 : 
        print ('Moça')
    else:
        print('Mulher')
elif sexo == 'M' or sexo == 'm':
    if idade <=12 :
        print('Menino')
    elif idade <= 24 : 
        print ('Rapaz')
    else:
        print('Homem')
else:
    print('Erro')

print('=)')