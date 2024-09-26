import ccp

menu=int(input('IMC(1) ou AREA(2)?'))
if menu==1:
    ccp.imc
    peso=float(input('Digite o seu peso kg: '))
    altura=float(input('Digite a sua altura em m:'))
    print(ccp.imc(peso,altura))

elif menu==2:
    base=float(input('Digite a base(m): '))
    altura=float(input('Digite a altura(m): '))
    print(ccp.area(base,altura))

else:
    print('entrada invalida!')