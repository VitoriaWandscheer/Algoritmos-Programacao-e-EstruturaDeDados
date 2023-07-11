    # QUESTÃO 3 (Maior/menor/0)

print('Digite [0] quando finalizarem os numeros a serem inseridos.')
val = int(input('Informe um número inteiro: '))
maior_valor = val
menor_valor = val
COND = 0

while val != COND:
    val = int(input('Informe um número inteiro: '))
    if val > maior_valor:
        maior_valor = val
    elif val < menor_valor and val != 0:
        menor_valor = val

print(f'O menor valor digitado foi {menor_valor}.')
print(f'O maior valor digitado foi {maior_valor}.')

print('=)')