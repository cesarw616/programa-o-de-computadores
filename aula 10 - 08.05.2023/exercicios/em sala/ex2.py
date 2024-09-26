num=input('digite um decimal: ')

binario=''
while num>0:
    binario=str(num%2)+binario
    num=num//2