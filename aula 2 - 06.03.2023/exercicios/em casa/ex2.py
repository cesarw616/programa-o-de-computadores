#- Escreva um programa em Python que solicite ao usuário o
#salário atual e mostre o salário acrescido de 5% de
#comissão
salario=float(input('Digite seu salário atual em reais: '))
comissao=(salario*(5*1/100))+salario
print(f'Seu salário com comissão é de {comissao} reais')