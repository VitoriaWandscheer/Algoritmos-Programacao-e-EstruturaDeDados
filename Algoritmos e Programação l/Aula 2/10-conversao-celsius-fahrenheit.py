# Alguns países medem temperaturas em graus Celsius, e outros em graus Fahrenheit.
# Faça um algoritmo para ler uma temperatura Celsius e imprimi-la em Fahrenheit
# (pesquise como fazer este tipo de conversão).

celsius = float(input('Digite a temperatura que deseja converter: '))

farenrait = celsius * 1.8 + 32

print (f'{celsius} graus Celsius equivalem a {farenrait} graus Fahrenheit.')

print('=)')