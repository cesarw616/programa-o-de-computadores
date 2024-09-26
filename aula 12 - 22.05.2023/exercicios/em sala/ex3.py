import ccp

while True:
    n1=float(input('Digite um numero: '))
    n2=float(input('Digite um numero: '))
    print(f'{n1}+{n2}={ccp.soma(n1,n2)}')

    if (input('Deseja continuar?')) in 'nN':break