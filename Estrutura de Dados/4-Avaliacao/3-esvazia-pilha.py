def esvaziaPilha():
    TAM = len(pilha)-1 # Armazena o índice do TOPO da pilha.
    # Percorre a pilha, de forma decrescente (do TOPO até a BASE), do último índice até o primeiro.
    for indice in range(TAM, -1, -1):
        # Mostra o elemento que será removido, ou seja, o elemento do TOPO.
        print('Retirada: ', pilha[indice])
        # Remove o elemento do TOPO
        pilha.remove(pilha[indice])

def cabecalho():
    print("\n----------   Vitória Wandscheer Pereira   ----------")
    print("-- Cursando Bacharelado em Sistemas de Informação --")
    print("-------------------      =)      -------------------")

cabecalho()

pilha = [0,1,2,3,4,5,6,7,8,9,10]

print("\nPilha inicial: ", pilha,"\n")
esvaziaPilha()
print("\nPilha Final: ", pilha,"\n")