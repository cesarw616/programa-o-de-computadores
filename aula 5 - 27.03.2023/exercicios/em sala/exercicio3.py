import os 
os.system ('cls')

print('Digite três números a serem comparados')
n1 = input('Digite o primeiro numero:')
n2 = input('Digite o segundo numero: ')
n3 = input('Digite o terceiro numero: ')

if n1>n2 and n1>n3:
    print(f'O maior é {n1}')
elif n2>n1 and n2>n3:
    print(f'O maior é {n2}')    
else:
    print(f'O maior é {n3}')

input('enter para continuar...')