num=input('digite um numero: ')
base=int(input('digite a base: '))

num=num.upper()
n= len(num)-1
num_conv= 0

dig = '0123456789ABCDEF'
for d in num:
    num_conv +=dig.find(d)*base**n
    n=n-1
print(num_conv)