# Um restaurante a quilo cobra R$45,00 o Kg de refeição.
# Escreva um algoritmo que
# leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar.
# Lembre-se que deve ser informado o peso do prato (tara),
# para que seja descontado do peso total.

QUILO = 45

peso = float(input('Informe o peso: '))
tara = float(input('Informe o peso do prato(tara): '))

valor = (peso - tara) * QUILO

print (f'O valor total a pagar é:\nR${valor}')

print('=)')