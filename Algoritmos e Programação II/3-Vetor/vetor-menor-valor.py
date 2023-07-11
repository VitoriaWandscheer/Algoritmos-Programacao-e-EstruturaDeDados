#   Faça um programa que preencha um vetor com os modelos de cinco carros (exemplos de modelos: Fusca, Gol, Vectra, etc).
#   Carregue outro vetor com o consumo desses carros, isto é, quantos quilômetros cada um deles faz com um litro de combustível.
#   Calcule e mostre:
#       a)  O modelo do carro mais econômico; e 
#       b)  Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 Km.
import numpy as np

modelo = list()

N = 5
consumo = []
consumo = np.zeros(N)

print('======== Informe: ========')
for indice in range(0,N):
    aux_modelo = input('\n   Modelo: ')
    modelo.append(aux_modelo)
    consumo[indice] = input('   Km/l  : ')

economico = consumo[0]
mod_eco = 0
indice = 1

while indice < 5:
    if economico > consumo[indice]:
        economico = consumo[indice]
        mod_eco = indice
    indice += 1

parametro = 1000
for indice in range(0, N):
    consumo[indice] = parametro / consumo[indice]

print(f'======================================================================\nO carro mais econômico é o {modelo[mod_eco]}, consumindo apenas {consumo[mod_eco]:.2f} litros para percorrer 1000km.')
print(f'\nTabela de consumo a cada {parametro}km:')
for indice in range (0, N):
    print(f'{modelo[indice]} -> {consumo[indice]:.2f}\n')

print('=)')