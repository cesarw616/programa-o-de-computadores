notas=[6,7,6.5,4.8,8]
alunos=['Victor',' Fabiana','Carlos','Pietro','Cesar']
cont=0
soma=0
melhores=[]
for nota in notas:
    soma=(soma+nota)
    media=soma/len(notas)
print(media)

for i in range(len(notas)):
    if notas[i]>media:
        melhores.append(alunos[i])
        cont+=1
print(cont,melhores)