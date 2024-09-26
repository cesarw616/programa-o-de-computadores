import os
os.system('cls')

altura=float(input('Digite sua altura: '))
gênero=input('Digite seu gênero: ')
pesoidealm= (72.7*altura)-58
pesoidealf= (62.1*altura) -44.7
if gênero == 'Homem' or 'homem':
    print(pesoidealm)
elif gênero == 'Mulher' or 'mulher':
    print(pesoidealf)
else:
    print('Você esqueceu algum campo')
