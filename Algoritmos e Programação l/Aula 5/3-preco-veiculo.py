# O custo ao consumidor de um carro novo é 
# a soma do preço de fábrica
# com o percentual de lucro do distribuidor e dos impostos aplicados ao preço de fábrica.
# Faça um programa que receba
# o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos,
# calcule e mostre:
# a. O valor correspondente ao lucro do distribuidor;
# b. O valor correspondente aos impostos;
# c. O preço final do veículo;

preco_fabrica = float(input('Informe o preço de fábrica do veiculo: '))
per_lucro = float(input('Informe o percentual de lucro: '))
per_imposto = float(input('Informe o percentual de impostos: '))

lucro_dist = (per_lucro * preco_fabrica) / 100
valor_imp = (per_imposto * preco_fabrica) / 100
preco_final = preco_fabrica + lucro_dist + valor_imp

print(f'O lucro do distribuidor é de R${lucro_dist:.2f}')
print(f'O valor correspondente aos impostos é de R${valor_imp:.2f}')
print(f'O preço final do veículo é de R${preco_final:.2f}')

print('=)')