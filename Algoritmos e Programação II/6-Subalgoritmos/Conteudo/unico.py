###################################################
################## FUNÇÃO #########################
###################################################

# 1
def maior(x,y):
    if x > y:
        print(f'\n[1] Entre os valores {x} e {y}, o maior valor é {x}.')
    else:
        print(f'\n[1] Entre os valores {x} e {y}, o maior valor é {y}.')

# 2
def par(x):
    if x % 2 == 0:
        return "TRUE"

# 3
def area_quadrado(x):
    return x ** 2

# 4
def area_triangulo(x,y):
    return (x * y) / 2

###################################################
############# RECEBENDO VALORES ###################
###################################################

x = int(input('Informe o valor de A:\n= '))
y = int(input('Informe o valor de B:\n= '))

###################################################
############# MOSTRANDO NA TELA ###################
###################################################

maior(x,y)
print('[2]', par(x))
print(f'[3] A área do quadrado de lado {x} é {area_quadrado(x)}.')
print(f'[4] A área do triângulo de base {x} e altura {y} é {area_triangulo(x,y)}')

print('\n=)')