def linha():
    print()
    print(40*'_')
    print()

def cabecalho():
    print(15*'_')
    print("----------   Vitória Wandscheer Pereira   ----------")
    print("-- Cursando Bacharelado em Sistemas de Informação --")
    print("-------------------      =)      -------------------")
    print(15*'_')


def inclui_na_pilha():
    print('Informe um valor para a pilha: ')
    pilha.append(input('Valor: '))

def retira_da_pilha():
    pilha.remove()

N = int(input('Informe o tamanho da PILHA: '))
pilha = []
linha()
print(f"Pilha vazia: {pilha}")
linha()

def assina():
    print()
    print('=)')
    print()

choice = 1
while (choice != 0) and (len(pilha) < N):
    inclui_na_pilha()
    linha()
    print("Informe [0] para NÃO ou [1] para SIM:")
    choice = int(input("Continuar? "))
    linha()

linha()
print(f"Pilha: {pilha}")
linha()

assina()