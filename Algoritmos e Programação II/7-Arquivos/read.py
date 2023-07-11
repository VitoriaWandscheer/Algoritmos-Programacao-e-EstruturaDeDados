# Abrindo um arquivo e lendo o seu conteúdo com FOR:
arquivo = open("aula.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close

# Abrindo um arquivo e lendo o seu conteúdo usando WITH:
with open ("aula.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)

print('=)')