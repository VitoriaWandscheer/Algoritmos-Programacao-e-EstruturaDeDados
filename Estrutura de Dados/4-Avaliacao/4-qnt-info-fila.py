def qtdElemento():
    global r, f
    print(f"Ré: {r} | Frente: {f}")
    print("A fila possuí {",len(fila),"} informações no momento.")

def preencheFila():
    global r, tam
    elemento = 1
    while r < tam:
        fila.append(elemento)
        r += 1
        elemento += 1

def remove():
    global f
    f += 1
    fila.remove(fila[f])

def cabecalho():
    print("\n----------   Vitória Wandscheer Pereira   ----------")
    print("-- Cursando Bacharelado em Sistemas de Informação --")
    print("-------------------      =)      -------------------")

cabecalho()

fila = []
tam = 5
f = -1
r = -1

preencheFila()

print()
print("Fila inicial: ",fila)
qtdElemento()
print()
remove()
print("Fila final: ",fila)
qtdElemento()
print()
remove()
print("Fila final: ",fila)
qtdElemento()
print()