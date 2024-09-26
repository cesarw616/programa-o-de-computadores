import os, math
os.system('cls')

a=float(input('Digite o valor de a: '))
b=float(input('Digite o valor de b: '))
c=float(input('Digite o valor de c: '))

delta=b**2-(4*a*c)

if delta<0:
    print('A equação não possui raízes reais.')
elif delta==0:
    print(f'A equação possui apenas uma raíz real, e seu valor é {(-b+(math.sqrt(delta)))/(2*a)}')
else:
    print(f'A equação tem duas raízes com valores {(-b+(math.sqrt(delta)))/(2*a)} e {(-b-(math.sqrt(delta)))/(2*a)}')

input('enter para continuar...')