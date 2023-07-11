# Criar um algoritmo que leia dez números inteiros
# e imprima o maior e o menor número. 
#
# NUMEROS INFORMADOS PELO USUARIO
#
print('Informe dez números: ')
a = int(input('= '))
b = int(input('= '))
c = int(input('= '))
d = int(input('= '))
e = int(input('= '))
f = int(input('= '))
g = int(input('= '))
h = int(input('= '))
i = int(input('= '))
j = int(input('= '))
#
# TESTANDO O MAIOR
#
maior = a
if maior < b :
    maior = b
if maior < c :
    maior = c
if maior < d :
    maior = d
if maior < e :
    maior = e
if maior < f :
    maior = f
if maior < g :
    maior = g
if maior < h : 
    maior = h
if maior < i :
    maior = i
if maior < j :
    maior = j
#
#  TESTANDO O MENOR
#
menor = a
if menor > b :
    menor = b
if menor > c :
    menor = c
if menor > d :
    menor = d
if menor > e :
    menor = e
if menor > f :
    menor = f
if menor > g :
    menor = g
if menor > h : 
    menor = h
if menor > i :
    menor = i
if menor > j :
    menor = j
#
# MOSTRANDO NA TELA O MAIOR E O MENOR DENTRE OS NUMEROS INFORMADOS PELO USUÁRIO
#
print(f'O maior número é {maior} e o menor é {menor}')
#
print('=)')