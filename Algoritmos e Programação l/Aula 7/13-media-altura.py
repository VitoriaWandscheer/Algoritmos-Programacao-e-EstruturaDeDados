# Escreva um algoritmo, que leia um conjunto de 10 fichas, cada uma contendo,
# a altura e o código do sexo de uma pessoa (código = 1 se for masculino e 2 se for feminino),
# e calcule e imprima: 
#   a maior e a menor altura da turma; 
#   a média de altura das mulheres; 
#   a média de altura da turma. 

cont = 0
soma_altura = 0
maior_alt = 0
menor_alt = 0
total_mulher = 0        # Contador
soma_alt_mulher = 0     # Acumulador

while cont < 10:
    sexo = int(input('Informe o código(1 para masculido e 2 para feminino): \n'))
    altura = float(input('Informe a altura: \n'))
   
    soma_altura = soma_altura + altura     # Soma todas as alturas
   
    if cont == 0 :         # Na primeira execução atribui o primeiro valor para cada variavel (maior e menor alturas)
        maior_alt = altura          
        menor_alt = altura
    
    if maior_alt < altura :        # Verifica a maior altura
        maior_alt = altura
    if menor_alt > altura:         # Verifica a menor altura
        menor_alt = altura

    if sexo == 2 : # SE FOR MULHER
        total_mulher = total_mulher + 1                 # Conta quantas mulheres há
        soma_alt_mulher = soma_alt_mulher + altura      # Soma de todas as altura informadas
    
    cont = cont + 1

if (total_mulher != 0) :
    media_alt_mulher = soma_alt_mulher / total_mulher

media_alt_turma = soma_altura / cont

print(f'A maior altura é: {maior_alt}')
print(f'A menor altura é: {menor_alt}')
if (total_mulher != 0) :
    print(f'A media das alturas das mulheres é {media_alt_mulher}')
print(f'A media das alturas da turma é {media_alt_turma}')

print('=)')