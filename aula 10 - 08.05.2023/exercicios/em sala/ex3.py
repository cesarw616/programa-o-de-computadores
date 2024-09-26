num=int(input('Digite um númerp decimal: '))

hexa=''
dig='0123456789ABCDEF'
while num>0:
    hexa=dig[num%16]+hexa
    num=num//16
print(hexa)