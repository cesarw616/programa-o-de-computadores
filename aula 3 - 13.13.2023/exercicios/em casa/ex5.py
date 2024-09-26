#Faça uma programa em Python que peça do usuário um valor em graus para um
#ângulo. Converta-o para radianos e, usando funções da biblioteca math, imprima o
#seno, cosseno e tangente deste ângulo.

import math
import os
os.system

g=math.radians(float(input('Digte o valor do ângulo em graus:')))
cos=math.cos(g)
sen=math.sin(g)
tan=math.tan(g)

print(f'Convertendo o ângulo para radiano, cosseno, seno e tangente, temos: \n{g} \n{cos} \n{sen} \n{tan}')

input('aperte enter para continuar...')