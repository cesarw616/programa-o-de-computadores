medias=[]
alunos=[]

while True:
    aluno=input('digite o nome do aluno: ')
    n1=float(input(f'digite a primeira do {aluno}: '))
    n2=float(input(f'digite a segunda nota do {aluno}'))
    media=(n1+n2)/2
    alunos.append(aluno)
    medias.append(media)
    resp=input('dseja continuar?')
    if resp in 'nN':break

print(30*'-')

for n, aluno in enumerate(alunos):
    print(f'[{n}]-{aluno}')
print(30*'-')

n=int(input('digite o numero do aluno: '))
resultado= if medias[n]>=6.0: print('Aprovado') else: print('Reprovado')
print(f'{resultado}')
