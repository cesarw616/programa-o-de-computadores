numeroDecimal=int(input('digite um numero: '))




n=numeroDecimal*1

binario=' '
while n>0:
    r=n%2
    binario=str(r)+binario
    n=n//2
print(binario)

hexa=' '
while n>0:
    r=n%16
    hexa=str(r)+hexa
    n=n//16
print(hexa)


octal=' '
while n>0:
    r=n%8
    octal=str(r)+octal
    n=n//8
print(octal)