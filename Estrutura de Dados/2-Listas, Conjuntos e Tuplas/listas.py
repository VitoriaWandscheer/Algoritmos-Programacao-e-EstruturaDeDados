
lista = []

def insere_elemento_lista(elemento):
    lista.append(elemento)

def remove_elemento_lista(elemento):
    lista.remove(elemento)

def tamanho_lista():
    print('Tamanho da lista: ', len(lista))

def insere_elemento_posicao_lista(posicao, elemento):
    if posicao >= len(lista):
        insere_elemento_lista(elemento)
    else:
        lista.insert(posicao, elemento)

def consulta_elemento_lista(elemento):
    if elemento in lista:
        for posicao in range(0, len(lista)):
            if lista[posicao] == elemento:
                print(f"A posição do elemento '{elemento}' na lista é: {posicao}")
    else:
        print(f"O elemento {elemento} não está na lista")

def linha():
    print(15*'_')

def assina():
    print()
    print('=)')
    print()

N = int(input('Informe o tamanho da lista: '))
i = 0
while i < N:
    insere_elemento_lista(int(input('Informe um valor para a lista: ')))
    i += 1

linha()
print(lista)
linha()
remove_elemento_lista(lista[2])
print(lista)
linha()
tamanho_lista()
linha()
insere_elemento_posicao_lista(10, 2)
print(lista)
linha()
consulta_elemento_lista(1)
linha()

assina()