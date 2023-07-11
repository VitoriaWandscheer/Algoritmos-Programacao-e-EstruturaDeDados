# Construa um algoritmo para determinar se o indivíduo está com um peso favorável.
# Essa situação é determinada através do IMC (Índice de Massa Corpórea),
# que é definida como sendo a relação entre o peso (PESO) e o quadrado da Altura (ALTURA) do indivíduo.
# Ou seja, imc = peso/altura^2

nome = str(input('Olá, qual seu nome? '))
peso = float(input(f'{nome} informe seu peso: '))
altura = float(input(f'Agora informe sua altura: '))

imc = peso / (altura ** 2)

ABAIXO = 20
NORMAL = 25
SOBRE = 30
OBESO = 40

if imc < ABAIXO : 
    print(f'{nome} você está abaixo do peso.')

if imc >= ABAIXO and imc < NORMAL : 
    print(f'{nome} você está com o peso normal.')

if imc >= NORMAL and imc < SOBRE :
    print(f'{nome} você está com sobre peso.')

if imc >= SOBRE and imc < OBESO :
    print(f'{nome} você está com obesidade.')

if imc >= OBESO :
    print(f'{nome} você está com obesidade mórbida.')

print('=)')