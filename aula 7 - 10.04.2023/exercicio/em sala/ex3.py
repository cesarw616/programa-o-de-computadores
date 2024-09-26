




b=input('digite um numero binario:')[::-1]
e=0
soma=0
for i in (b):
    n=int(i)
    d=(n*(2**e))
    e=e+1
    soma=soma+d
    print(i)
print(f'decimal: {soma}')

b=input('digite um numero binario:')[::-1]
e=0
soma=0
for i in (b):
    n=int(i)
    d=(n*(16**e))
    e=e+1
    soma=soma+d
    print(i)
print(f'hexaBin: {soma}')

b=input('digite um numero binario:')[::-1]
e=0
soma=0
for i in (b):
    n=int(i)
    d=(n*(8**e))
    e=e+1
    soma=soma+d
    print(i)
print(f'octaBin: {soma}')