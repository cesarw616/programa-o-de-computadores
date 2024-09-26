#Faça um programaque solicite ao usurio dois valores e, em seguida,
#calcule a media desses valores e imprima na tela.
import os
os.system('cls' or 'clear')

v1=float(input('Digite um numero: '))
v2=float(input('Digite outro numero: '))
media=(v1+v2)/2
print(f'A média entre os dois valores é:{media:.2f}')