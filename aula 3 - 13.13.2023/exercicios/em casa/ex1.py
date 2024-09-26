#Faça um programa em Python que calcule e mostre o valor do volume do tronco de
#uma pirâmide, para isso o programa deve solicitar ao usuário os valores da altura do
#tronco da pirâmide (h), o valor da base menor (Bmenor) e o da base maior (Bmaior) e
#calcular a seguinte expressão:

import math
import os
os.system

h=float(input ('Digite o valo da altura:'))
b1=float(input('Digite o valor da base maior: '))
b2=float(input('Digite o valor da base menor:'))
v=h/(3*(math.sqrt (b1**2+b2**2+(b1**2*b2**2))))
print(f'o volume da pirâmide é: {v:.2f}')

input('aperte enter para continuar...')