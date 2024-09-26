import os, math
os.system('cls')

n1=float(input('Digite o primeiro número: '))
n2=float(input('Digite o segundo número: '))
op=input('Qual operação gostaria de realizar(sm,sb,mult,div): ')

if op=='sm':
    print(f'O resultado é: {n1+n2}')
elif op=='sb':
    print(f'O resultado é: {n1-n2}')
elif op=='mult':
    print(f'O resultado é: {n1*n2}')
elif op=='div':
    print(f'O resultado é: {n1/n2}')
else:
    print('Entrada inválida.')

input('enter para continuar...')