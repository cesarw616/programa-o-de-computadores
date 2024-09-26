import math
import os
os.system('cls')
p=float(input('Digite seu peso em quilos: '))
h=float(input('Digite sua altura em metros: '))

IMC=p/(h**2)

if IMC<20:
    print('Você está abaixo do peso')
elif IMC<25:
    print('Você está com o peso ideal')
elif IMC<30:
    print('Você está com o sobrepeso')
elif IMC<35:
    print('Você está obeso')
else:
    print('Vocë está com obesidade mórbida')

input('enter para continuar...')