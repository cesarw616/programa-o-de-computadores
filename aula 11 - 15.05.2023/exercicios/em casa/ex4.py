nomes=[]
notas=[]
cursos=[]
soma=0
acima=0

for i in range(3)
    nome=input('Digite o nom do aluno: ')
    nomes.append(nome)
    nota=float(input(f'Digite a nota do aluno {nome}: '))
    notas.append(nota)
    soma=soma+nota
    curso=input(f'Digite o curso do aluno {nome}: ')
    cursos.append(curso)

tads=cursos.count('tads')
print(tads)

media=soma/10
print(media)

for nota in notas:
    if nota > media:
        acima+=1
print(acima)