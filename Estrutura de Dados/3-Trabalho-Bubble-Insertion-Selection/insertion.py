# Vitória Wandscheer Pereira
# Atividade Listas Ordenadas I
# Insertion Sort

lista = [2,0,3,1]
print("\nOriginal       => ", lista)

# Percorre a lista a partir do segundo elemento, armazenando-o como "Elemento Chave".
# Armazena a posição do elemento anterior ao elemento chave.
for elemento in range(1, len(lista)):
    elemento_chave = lista[elemento]
    esquerda = elemento-1
    # Verifica se o índice a esquerda do elemento chave é um índice "existente".
    # Verifica se o elemento chave é menor que o/os elemento/s a sua esquerda.
    # Se ambas forem verdade, move o elemento uma posição a frente,
    # bem como decresce um indice,
    # até que todos os elementos a esquerda do elemento chave sejam verificados.
    while (esquerda >= 0) and (elemento_chave < lista[esquerda]):
        lista[esquerda+1] = lista[esquerda]
        esquerda -= 1
    # Após a verificação e as mudanças de posição dos elementos maiores que a chave,
    # insere-se o elemento chave em sua posição correta.
    lista[esquerda+1] = elemento_chave

print("Insertion Sort => ", lista)

print("\n=)\n")