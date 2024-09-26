#Desenvolva um programa em Python que solicite ao
#usuário os valores dos lados de um retângulo e calcule e
#mostre seu perímetro e sua área.

lado=int(input('Digite o valor do lado do retângulo em cm: '))
base=int(input('DIgite o valor da base do retângulo em cm: '))
area=lado*base
perimetro=(2*lado)+(2*base)
print('A área do retângulo é de %s cm², e o perímetro é de %s cm' % (area,perimetro))