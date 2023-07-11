# Ler um arquivo e gravar em outro

with open ('multipos_de_4.txt', 'w+') as multiplos4:
    with open ('pares.txt', 'r+') as pares:
        for linha in pares.readlines():
            if int(linha) % 4 == 0:
                multiplos4.write(f'{linha}\n')