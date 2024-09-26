import os, math
os.system('cls')

n1=float(input('Digite um número real: '))
n2=float(input('Digite outro número real: '))
op=input('Digite uma operação para realizar com os números(media, sub, mult, div): ')

media=(n1+n2)/2
sub=math.fabs(n1-n2)
mult=n1*n2
div=n1/n2

if op=='media':
    print(media)
elif op=='sub':
    print(sub)
elif op=='mult':
    print(mult)
elif op=='div':
    print(div)
else:
    print('Entrada inválida!')
