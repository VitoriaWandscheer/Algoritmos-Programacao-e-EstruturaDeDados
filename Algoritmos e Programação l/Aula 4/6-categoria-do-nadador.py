# A confederação brasileira de natação irá promover eliminatórias para o próximo mundial.
# Fazer um algoritmo que receba a idade de um nadador
# e determine (imprima) a sua categoria segundo a tabela a seguir:
#
#   CATEGORIA:     IDADE:
#   infantil A     5 a 7
#   infantil B     8 a 10
#   juvenil A      11 a 13
#   juvenil B      14 a 17
#   senior         maiores de 18

nome = str(input('Olá, informe o nome do(a) nadador(a): '))
idade = int(input('Informe a idade do(a) nadador(a): '))

INF_A = 5
INF_B = 8
JUV_A = 11
JUV_B = 14
SEN = 18

if idade >= INF_A and idade < INF_B : 
    print(f'{nome} está na categoria Infantil A.')

if idade >= INF_B and idade < JUV_A : 
    print(f'{nome} está na categoria Infantil B.')

if idade >= JUV_A and idade < JUV_B :
    print(f'{nome} está na categoria jUVENIL A.')

if idade >= JUV_B and idade < SEN :
    print(f'{nome} está na categoria Juvenil B.')

if idade >= SEN :
    print(f'{nome} está na categoria Sênior.')

print('=)')