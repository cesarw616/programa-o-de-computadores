#Crie um programa em Python que solicite ao usuário a sua idade expressa em
#anos, meses e dias (variáveis separadas). Calcule e mostre a idade expressa apenas
#em dias. Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.

import math
import os
os.system

a=int(input('Digite seus anos de idade:'))
m=int(input('Digite quantos meses ja tem desde seu útlimo ano completo:'))
d=int(input('Digite quantos dias tem desde seu último mês completo:'))

dias=(a*365)+(m*30)+d 

print(f'Sua idade equivale a {dias} dias')

input('aperte enter para continuar...')