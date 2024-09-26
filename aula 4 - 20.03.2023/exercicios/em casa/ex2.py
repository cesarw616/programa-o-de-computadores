import os
os.system('cls')

turno=(input('Digite seu turno de trabalho (N/D): '))
horas=float(input('Digite o seu total de horas trabalhadas: '))

if turno == 'N' or 'n':
    print(f'O salário a ser pago é de R$ {45*horas:.2f}')
elif turno == 'D' or 'd':
    print(f'O salário a ser pago é de R$ {37.5*horas:.2f}')
else:
    print('Entrada inválida!')

input('enter para continuar...')