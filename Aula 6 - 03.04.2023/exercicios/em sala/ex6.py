a1=float(input('Digite o valor da sua primeira nota: '))
a2=float(input('Digite o valor da  sua segunda nota: '))
media= (a1+a2)/2
if media < 4:
    print("E - Reprovado")
elif media < 6:
    print('D - Reprovado')
elif media < 7.5:
    print('C - Aprovado')
elif media < 9:
    print('B - Apovado')
else:
    print('A - Aprovado')