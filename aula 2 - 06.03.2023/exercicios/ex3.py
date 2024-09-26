#Faça uma calculadoraem python que solicite ao usuario dois valores e,
#em seguida imprima as operações matematicas de soma, subtração,
#multiplicação, divisão e o resto da divisão desses numeros.

v1=float(input('Digite o valor 1: '))
v2=float(input('Digite o valor 2: '))
soma=v1+v2
subtração=v1-v2
multiplicação=v1*v2
divisão_int=v1//v2
divisão_frac= v1/v2
resto=v1%v2
print(f'Soma:{soma}\n Subtração:{subtração}\n Multiplicação:{multiplicação}')
print(f'Divisão inteira:{divisão_int}\n Resto:{resto}\n Divisão decimal:{divisão_frac}')
