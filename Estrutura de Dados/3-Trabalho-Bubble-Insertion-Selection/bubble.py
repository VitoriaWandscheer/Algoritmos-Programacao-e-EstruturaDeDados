# Vitória Wandscheer Pereira
# Atividade Listas Ordenadas I
# Bubble Sort

lista = [1,4,3,2,5,0]
print("\nOriginal    => ", lista)

# Percorre a lista por completo, garantindo que todos os elementos sejam verificados.
for x in range(0, len(lista)):
    # Percorre a lista item a item, comparando cada item com seu subsequente.
    # Obs.: O último item da lista não entra nesse laço, visto que sua verificação se da em conjunto com o penultimo item.
    # Caso a ordem esteja incorreta, corrige invertendo suas posições.
    for item in range(0, len(lista)-1):
        if lista[item] > lista[item+1]:
            lista[item], lista[item+1] = lista[item+1], lista[item]
        
print("Bubble Sort => ", lista)

print("\n=)\n")