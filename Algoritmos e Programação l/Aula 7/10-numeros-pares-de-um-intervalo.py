# Criar um algoritmo que
# LEIA os limites inferior e superior de um intervalo
# e IMPRIMA todos os NUMEROS PARES no intervalo aberto
# e seu SOMATORIO. 
inicio = int(input('Informe o limite inferior do intervalo:\n= '))
fim = int(input('Informe o limite superior do intervalo:\n= '))
PAR = inicio
x = inicio
while inicio >= x <= fim:
    if PAR % 2 == 0:
        print(PAR)
        inicio += 2
    else:
        PAR += 1
        print(PAR)

print('=)')