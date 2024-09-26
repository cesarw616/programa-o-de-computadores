#Escreva um programa em Python que leia um valor representando o gasto realizado
#por um cliente do restaurante ComaBem e visualize o valor total a ser pago,
#considerando os 10% do garçom

comanda=float(input('Digite o total da comanda: '))
garcom=(comanda*(10/100)+comanda)
txt='O total a ser pago pelo cliente é de {0:.2f} reais'
print(txt.format(garcom))