#Escreva um programa em Python que calcule as duas
#raízes de uma equação de 2º grau ax²+bx+c, conhecendo
#os valores dos coeficientes da mesma (a, b, c). Suponha
#que as raízes são reais.

a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor de c: '))

delta=(b*b)-(4*a*c)

x1=(-b+(1/delta*(1/delta)))/(2*a)
x2=(-b-(1/delta*(1/delta)))/(2*a)

print(f'As duas raízes são: x1={x1:.2f} e x2={x2:.2f}')