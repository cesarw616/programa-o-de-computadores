import os, math
os.system('cls')

p=input('Digite o nome do produto: ')
c=float(input('Digite o custo de compra do produto: '))

if c<10:
    print(f'O valor de venda de {p} é R$ {c*1.7}')
elif c<30:
    print(f'O valor de venda de {p} é R$ {c*1.5}')
elif c<50:
    print(f'O valor de venda de {p} é R$ {c*1.4}')
elif c>=50:
    print(f'O valor de venda de {p} é R$ {c*1.3}')

input('enter para continuar...')