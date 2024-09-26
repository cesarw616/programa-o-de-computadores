import os
os.system('cls')

i=int(input('Digite a sua idade: '))

if i<16:
    print('Você não pode votar.')
elif i>=16 and i<18:
    print('Voto facultativo.')
else:
    print('Você é obrigado a votar.')

input('enter para continuar...')    