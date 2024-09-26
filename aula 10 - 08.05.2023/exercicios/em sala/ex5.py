num=float(input('digite um numero: '))
valor=num+(num*0.05)

print(f'num = {valor:_.2f}'.replace('.',',').replace('_','.'))