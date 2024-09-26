import os, math
os.system('cls')

x=float(input('Digite a coordenada do ponto em X: '))
y=float(input('Digite a coordenada do ponto em Y: '))

if x>0 and y>0:
    print('o ponto está no 1º quadrante.')
elif x<0 and y>0:
    print('o ponto está no 2º quadrante.')
elif x<0 and y<0:
    print('o ponto está no 3º quadrante.')
else:
    print('o ponto está no 4º quadrante.')

input('enter para continuar...')