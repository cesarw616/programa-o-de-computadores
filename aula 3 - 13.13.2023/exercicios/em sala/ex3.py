import os
import math
os.system

n=float(input('Digite um numero real: '))
a=math.fabs(n)
b=math.floor(n)
c=math.sqrt(n)
d=math.factorial(math.floor(math.ceil(n)))

print(f'A: {a} \nB:{b} \nC:{c} \nD:{d}')