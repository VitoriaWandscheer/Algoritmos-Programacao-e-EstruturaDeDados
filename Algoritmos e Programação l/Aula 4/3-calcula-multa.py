# Escreva um programa que pergunte a velocidade do carro de um usuário.
# Caso o valor informado seja maior que 80km/h,
# exiba uma mensagem dizendo que o usuário foi multado. 
# Neste caso, exiba o valor da multa , cobrando R$ 5,00 por Km acima dos 80 km/h.

velocidade = int(input('Informe a velocidade do carro: '))
MAX = 80 # Velocidade máxima: 80km/h

if velocidade > MAX : 
    multa = 5 * (velocidade - MAX) # R$5,00 por km/h acima do permitido.
    print('Você foi multado :( ')
    print(f'Sua multa é de R${multa}.')
else : 
    print('Parabéns! você NÃO foi multado :) ')

print('=)')