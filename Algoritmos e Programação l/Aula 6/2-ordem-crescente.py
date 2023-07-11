# Faça um algoritmo que lê valores para 
# 3 variáveis A, B e C e mostra as mesmas em ordem crescente.

a = int(input('Informe um valor: '))
b = int(input('Informe outro valor: '))
c = int(input('Agora mais um valor: '))

if (a < b) and (a < c) :
    if b < c :
        print(a, b, c)
    else:
        print(a, c, b)
elif (b < a) and (b < c) : 
    if a < c :
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a < b :
        print(c, a, b)
    else:
        print(c, b, a)

print('=)')