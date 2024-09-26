a1=float(input('Digite a nota a1: '))
a2=float(input('Digite a nota a2: '))
media=(a1+a2)/2

if media<4:
    print('E - Reprovado')
elif media<6:
    print('D - Reprovado')
elif media<7.5:
    print('C - Aprovado')
elif media<9:
    print('B - Aprovado')
else:
    print('A - Aprovado')

input('enter para continuar...')


