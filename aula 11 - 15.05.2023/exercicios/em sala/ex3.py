lista=[]
while True:
    num=int(input('digite um numero inteiro: '))
    if num==0:
        break
    lista.append(num)
media=sum(lista)/len(lista)
print(lista)
print(f'{media:.2f}')
