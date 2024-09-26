#inverso de um numero

import os
os.system ('cls' or 'clear')

n=542
d1=n//100
d2=n%100//10
d3=542%10
inverso=d3*10**2+d2*10+d1
print(f'Número:{d1}{d2}{d3} \nInverso do número:{inverso}')

input('Aperte enter para continuar...')