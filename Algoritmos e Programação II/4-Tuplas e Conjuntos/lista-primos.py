# Preencha uma estrutura (lista, tupla ou conjunto) com 9 números inteiros,
# calcule e mostre os números primos e suas respectivas posições na estrutura.

lista = [0, 0, 0, 0, 0, 0, 0, 0, 0]
primos = list()

print('Informe:')
for x in range(0, 9):
    lista[x] = int(input('= '))
    aux = lista[x]
    cont = 0
    if aux == 2:
        primos.append(aux)
        primos.append(x)
        cont += 1
    if aux > 2:
        for z in range(2, aux):
            if (aux % z) == 0:
                cont += 1
    if cont == 0:
        primos.append(aux)
        primos.append(x)

if len(primos) != 0:
    print(f'Dentre os valores {lista}, são números primos e suas respectivas posições:')
    qtd = int(len(primos))
    for x in range(0, qtd, 2):
        print(f'Número: {primos[x]}           Posição: {primos[x+1]}')
else:
    print(f'Dentre os valores [{lista}], não há números primos.')

print('=)')