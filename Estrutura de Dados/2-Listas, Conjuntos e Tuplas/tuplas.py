def tamanho_tupla():
    print('Tamanho da tupla: ', len(tupla))

def consulta_elemento_tupla(elemento):
    if elemento in tupla:
        for posicao in range(0, len(tupla)):
            if tupla[posicao] == elemento:
                print(f"A posição do elemento '{elemento}' na tupla é: {posicao}")
    else:
        print(f"O elemento {elemento} não está na tupla {tupla}")

def linha():
    print(15*'_')

def assina():
    print()
    print('=)')
    print()

tupla_vazia = ()
print("Tupla vazia: ", tupla_vazia)
tupla = (10,20)
linha()
print('Exemplo de tupla: ', tupla)
linha()
print("Tipo de uma tupla: ", type(tupla))
linha()

# | Extrair elementos individuais de uma tupla | #
x, y = tupla
print('Elementos individuais de uma tupla: ')
print("x =", x)
print("y =", y)
linha()
tamanho_tupla()
linha()
consulta_elemento_tupla(11)
linha()

assina()