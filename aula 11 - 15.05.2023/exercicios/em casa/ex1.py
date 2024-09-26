valores=[]
par=[]
impar=[]

while True:
    num=int(input('Digite um numero inteiro: '))
    valores.append(num)
    if num%2==0:
        par.append(num)
    else:
        impar.append(num)
    repete=input('Deseja adicionar outro numero a lista?(S/N)')
    if repete in 'nN': break
print(valores, par, impar)