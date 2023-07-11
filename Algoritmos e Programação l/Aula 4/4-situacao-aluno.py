# Construa um algoritmo para determinar a situação (APROVADO/EXAME/REPROVADO) de um aluno
# dado a sua frequência (FREQ) (porcentagem de 0 a 100%)
# e sua nota (NOTA) (nota de 0.0 a 10.0), segundo a tabela...

nome = str(input('Informe o nome do(a) aluno(a): '))
freq = int(input('Informe a frequênia: '))
nota = float(input('Informe a nota: '))

FREQ = 75
MIN = 3.0
MED = 7.0

if freq < FREQ :
    print(f'{nome} está REPROVADO(A) pois sua frequencia foi inferior a {FREQ}%\nhaha, de tanto matar aula ela te matou')
 
if freq >= FREQ and nota < MIN  :
    print(f'{nome} está REPROVADO(A) pois sua nota foi inferior a {MIN}.\nEita, se fudeu legal :( ')

if freq >= FREQ and nota >= MIN and nota < MED :
    print(f'{nome} está em EXAME pois sua nota foi inferior a {MED} e superior a {MIN}.\nSe esforça que ainda da tempo :)')


if freq >= FREQ and nota >= MED :
    print(f'{nome} está APROVADO(A) pois sua frequencia e sua nota estão top top.\nParabéns :)')

print('=)')