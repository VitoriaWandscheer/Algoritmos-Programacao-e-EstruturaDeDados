# Ler 2 duas estruturas (lista, tupla ou conjunto), denominada R de 5 elementos e S de 10 elementos, ambos de inteiros.
# Gere outra estrutura X que possua os elementos comuns a R e a S. Considere que na mesma estrutura não haverá números repetidos. 

R = [0, 0, 0, 0, 0]                     # 
S = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]      # 
X = set()                               # Criando o conjunto "X"

print('Informe os 5 valores para R:')
for indice_r in range(0, 5):
    R[indice_r] = int(input('= '))

print('\nInforme os 10 valores para o vetor S:')
for indice_s in range(0, 10):
    S[indice_s] = int(input('= '))

for indice_r in range(0, 5):
    for indice_s in range(0, 10):
        if R[indice_r] == S[indice_s]:
            X.add(S[indice_s])

print(f'A extrutura contendo os elementos comuns a R e S é igual ao conjunto X={X}')

print('=)')