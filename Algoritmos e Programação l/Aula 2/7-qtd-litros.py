# Um motorista deseja colocar no seu tanque X reais de gasolina.
# Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento,
# e exibir quantos litros ele conseguiu colocar no tanque.

reais = float(input('Quantos reais de gasolina você deseja colocar em seu tanque?\nR$'))
preco_litro = float(input('Qual o preço por litro de gasolina?\nR$'))

litros_tanque = reais / preco_litro

print (f'Foram colocados {litros_tanque} litros de gasolina no tanque.')

print('=)')