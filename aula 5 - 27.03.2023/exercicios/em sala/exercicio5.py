t=float(input('Digite o valor total da compra: '))
p=int(input('Opções de parcelamento disponíveis: 2 \n4 \n6 \n8 \nDigite a quantidade de parcelas: '))

if p==2:
    print(f'{(t*1.03):.2f}')
elif p==4:
    print(f'{(t*1.07):.2f}')
elif p==6:
    print(f'{(t*1.09):.2f}')
elif p==8:
    print(f'{(t*1.12):.2f}')
else:
    print('Parcelamento indisponivel!')

input('enter para continuar...')