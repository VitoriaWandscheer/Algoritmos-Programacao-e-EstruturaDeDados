    # QUESTÃO 06 (intervalo de numeros)
print('Digite um número negativo quando finalizarem os valores a serem inseridos.')
print('Informe os valores (em números inteiros): ')

num = 1
inter_1 = 0
inter_2 = 0
inter_3 = 0
inter_4 = 0

while num >= 0:
    num = int(input('= '))
    if 0 <= num <= 25:
        inter_1 += 1
    elif 25 < num <= 50:
        inter_2 += 1
    elif 50 < num <=75:
        inter_3 += 1
    elif 75 < num <= 100:
        inter_4 += 1

print('Estão entre os intervalos:')
print(f'[000-025] -> {inter_1} número(s).')
print(f'[026-050] -> {inter_2} número(s).')
print(f'[051-075] -> {inter_3} número(s).')
print(f'[076-100] -> {inter_4} número(s).')

print('\n\n\n=)')