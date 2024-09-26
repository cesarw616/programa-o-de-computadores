import os


soma=lambda a,b: a+b
subt=lambda a,b: a-b
multi=lambda a,b: a*b
div=lambda a,b: a/b
menu= ['soma', 'subtração', 'multiplicação', 'divisao', 'sair']

while True:
    os.system ('cls' or 'clear')
    for n, item in enumerate(menu):
        print(f'[{n+1}]-{item}')
    op=int(input('>>Digite uma opção: '))

    if op==5:break
    elif str(op) not in '1234': print('Opção inválida!')
    else:
        n1=float(input('Digite o primeiro número: '))
        n2=float(input('Digite o segundo número: '))

        if op==1: print(f'{n1}+{n2}={soma(n1,n2)}')
        elif op==2: print(f'{n1}-{n2}={subt(n1,n2)}')
        elif op==3: print(f'{n1}.{n2}={multi(n1,n2)}')
        else: print(f'{n1}/{n2}={div(n1,n2)}')
    input('aperte enter para continuar...')