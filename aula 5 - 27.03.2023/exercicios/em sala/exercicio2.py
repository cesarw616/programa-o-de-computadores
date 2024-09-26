import os
os.system('cls')

dias=int(input('Digite a quantidade de dias que gostaria de se hospedar: '))
valor=input('Digite o seu tipo de diária \nSimples[S] \nDupla[D] \nTripla[T] \n: ')

if valor in 'Ss':
    print(f'O total será de {dias*255.5} reais')
elif valor in 'Tt':
    print(f'O total será de {dias*305.5}')
elif valor in 'Dd':
    print(f'O valor total será de {dias*360.5} reais')
else:
    print('Entrada inválida!')

    input('enter para continuar...')