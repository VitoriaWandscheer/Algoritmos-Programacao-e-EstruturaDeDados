# Vitória Wandscheer Pereira
# Atividade Listas Ordenadas I
# Selection Sort

lista = [2,0,10,3,1]
print("\nOriginal       => ", lista)

# Percorre a lista a cada posição,
# armazenando o indice da posição atual como o menor valor.
for posicao in range(len(lista)):
    index_menor = posicao
    # Percorre a lista a partir do elemento subsequente ao assumido como menor valor.
    # Compara o valor assumido como menor com o restante dos itens a sua frente.
    # Caso o valor assumido como menor seja maior que o valor que esta se comparando,
    # atualiza-se o menor valor.
    for parametro in range(posicao+1, len(lista)):
        if lista[index_menor] > lista[parametro]:
            index_menor = parametro
    # Após encontrar o indice do menor valor da lista,
    # realoca-o na primeira posição não classificada,
    #  armazenando o valor que estava nessa posição no indice em que o menor valor estava.
    lista[posicao], lista[index_menor] = lista[index_menor], lista[posicao]

print("Selection Sort => ", lista)

print("\n=)\n")