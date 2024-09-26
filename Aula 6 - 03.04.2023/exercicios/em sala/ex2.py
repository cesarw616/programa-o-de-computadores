import os, math
os.system('cls')

s=int(input('Digite, em segundos, o tempo a ser convertido: '))

print(f'o tempo {s} em segundos equivale a {(s//3600)} horas, {(s%3600)//60} minutos e {(s%3600)%60} segundos')
input('enter para continuar...')