# Abrindo um arquivo e escrevendo com FOR:
arquivo = open ("aula.txt", "w")
for linha in range(1,101):
    arquivo.write(f"{linha}\n")
arquivo.close

# Abrindo um arquivo e escrevendo com WITH:
with open ("aula.txt", "w") as arquivo:
    for linha in range(1,101):
        arquivo.write(f"{linha}\n")

print('=)')