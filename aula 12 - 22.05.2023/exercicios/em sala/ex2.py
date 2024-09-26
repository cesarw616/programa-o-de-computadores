def media(a1,a2):
    return(a1+a2)/2

n1= float(input('Digite a nota 1: '))
n2= float(input('Digite a nota 2: '))

if media(n1,n2)>=6:
    print('Aprovado!')
else:
    print('Reprovado!')