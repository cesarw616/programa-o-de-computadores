import os, math
os.system ('cls')

compras=float(input('Digite o valor da compra: '))

if compras>200:
    print(f'O valor da compra com desconto é R${compras*0.8} ')
else:
    print(f'O valor da compra é R${compras} \nNão oferecemos desconto para valores abaixo de 200 reais.')

input('enter para continuar...')