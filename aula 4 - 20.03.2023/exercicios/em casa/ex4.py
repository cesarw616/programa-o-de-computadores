import os
os.system ('cls')

salario=float(input('Digite o seu salario em R$: '))
luz=float(input('Digite a sua conta de luz em R$: '))
agua=float(input('Digite a sua conta de agua em R$: '))
telefone=float(input('Digite da conta de telefone em R$: '))

total=salario-(luz+agua+telefone)

if total<0:
    print(f'Seu salário não é suficiente.')
else:
    print(f'Você conseguirá pagar todas as contas.')

input('enter para continuar...')
