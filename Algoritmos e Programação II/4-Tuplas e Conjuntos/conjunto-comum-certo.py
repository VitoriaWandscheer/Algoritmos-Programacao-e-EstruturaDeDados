### DECLARANDO CONJUNTOS ###
R = set()
S = set()
X = set()

### RECEBENDO VALORES DOS USUÁRIOS NOS CONJUNTOS CRIADOS ###
print('Informe os 5 valores para R:')
for x in range(0, 5):
    R.add(int(input('= ')))

print('\nInforme os 10 valores para S:')
for y in range(0, 10):
    S.add(int(input('= ')))

### ESTRUTURA X COM ELEMENTOS COMUNS A {R} E {S} ###
X = R & S

### MOSTRA AO USUARIO O CONJUNTO X ###
print(f'A extrutura contendo os elementos comuns a R e S é igual ao conjunto X={X}')

print('=)')