conjunto = set()

def insere_elemento_conjunto(elemento):
    conjunto.add(elemento)

def remove_elemento_conjunto(elemento):
    conjunto.discard(elemento)
    # a função 'discard' remove um elemento do conjunto se o elemento estiver presente mas não faz nada caso contrário
    # conjunto.remove(elemento) | Se o elemento não estiver presente, a função 'remove' causa uma exceção (erro)

def tamanho_conjunto():
    print('Tamanho do conjunto: ', len(conjunto))

def consulta_elemento_conjunto(elemento):
    if elemento in conjunto:
        print(f"O elemento '{elemento}' ESTÁ contido no conjunto {conjunto}")
    else:
        print(f"O elemento '{elemento}' NÃO ESTÁ contido no conjunto {conjunto}")

def linha():
    print(15*'_')

def assina():
    print()
    print('=)')
    print()

controle = 1
while controle == 1:
    insere_elemento_conjunto(int(input('Informe um valor para o conjunto: ')))
    controle = int(input('Deseja inserir mais elementos? | [0] Não | [1] Sim |'))

linha()
print(conjunto)
linha()
remove_elemento_conjunto(4)
print(conjunto)
linha()
tamanho_conjunto()
linha()
consulta_elemento_conjunto(10)
linha()

assina()