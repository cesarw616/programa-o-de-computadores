#Escreva um programa em Python para calcular o valor de uma prestação em atraso
#(prestacao). Para isso, obtenha o valor da prestação (valorPrestacao), a porcentagem
#de multa pelo atraso (multa) e a quantidade de dias de atraso (qtdeDias). Calcular e
#mostrar o valor da prestação atualizado, sabendo que:
#prestação = valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

import math
import os 
os.system

p=float(input('Digite o valor da parcela sem multa: '))
m=float(input('Digite o valor da multa:'))
d=int(input('Digite a quantidade de dias de atraso: '))
pm=p+(p*(m/100)*d)

print(f'O valor da parcela com multa é {pm}')

input('aperte enter para continuar...')