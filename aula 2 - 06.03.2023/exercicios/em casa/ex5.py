#Escreva um programa em Python que leia a cotação do
#dólar (taxa de conversão), leia um valor em dólares e converta e mostre o valor equivalente em Reais

reais=float(input('Digite a quantia em reais que você quer converter: '))
dolar=reais/5.22
txt='Você consegue converter {0:.2f} em {1:.2f}'
print(txt.format(reais,dolar))
