#Escreva um programa em python que analise se um aluno tem frequencia maior que 75%, e se a média dele é maior do que 6 e diga se ele está aprovado.

import os
os.system ('cls')

f=float(input('Digite a sua frequênia de aula em porcentagem: '))
m=float(input('Digite a sua média: '))

if f< 75:
 print('Você está reprovado por faltas!')
elif m < 6:
 print('Você está reprovado por nota!')
else:
  print('Você está aprovado!')

input('enter para continuar...')